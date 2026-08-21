# Guides

The step-by-step guides the manual carries beyond the core tasks: deployment, an installable theme,
the listing module, web fonts, and a front-end filter.

## Contents

- [Deploy with Deployer](#deploy-with-deployer)
- [Create an installable theme](#create-an-installable-theme)
- [Module Listing](#module-listing)
- [Using web fonts](#using-web-fonts)
- [Front end filter implementation](#front-end-filter-implementation)
- [Source](#source)

## Deploy with Deployer

**Source:** https://docs.contao.org/5.x/manual/en/guides/deployer/

This guide shows how to deploy a Contao project with Deployer, either by checking out a Git repository on the remote server or by uploading files with rsync, using rolling symlink releases.

**Info note:** the Deployer recipe is part of Deployer 7 and is intended to work for Contao 4.13 and higher.

### Install Deployer

1. If not done yet, install Deployer in the project:

```bash
composer require --dev deployer/deployer
```

2. Verify that Deployer runs in the minimum version *7.0* by running `vendor/bin/dep --version`.
3. Once done, create a `deploy.php` file in the project:

```bash
touch deploy.php
```

### Write deploy.php file

There are two ways to deploy the project to the remote site. The default approach to deploy files in Deployer is to check out the Git repository with the current project on the remote server.

#### Option 1: Deploy with Repository

1. Use the following file contents for the `deploy.php` in the project root:

```php
// deploy.php

namespace Deployer;

import('recipe/contao.php');

host('example.org')
    ->set('remote_user', 'foobar')
    ->set('deploy_path', '/var/www/{{remote_user}}/html/{{hostname}}')
    ->set('bin/php', 'php8.1')
    ->set('bin/composer', '{{bin/php}} /var/www/{{remote_user}}/composer.phar')
;

set('repository', 'git@github.com:acme/example.org.git');

set('keep_releases', 10);

after('deploy:failed', 'deploy:unlock');
```

2. Adjust the host configuration (per the Deployer documentation) and repository URL as required.

Caveats of the Git repo approach stated upstream: the local files always need to be committed and pushed; and in case the SSH environments do not support agent forwarding, the remote site needs read access on the Git repository, which requires storing the HTTPS credentials or configuring SSH. Therefore, another favored approach is to use `rsync` instead of Git.

#### Option 2: Deploy with rsync

To use `rsync` instead of a Git checkout, the `deploy:update_code` task is overridden:

```php
// deploy.php

/* Your existing config from "Option 1" */

// Not needed anymore
//-set('repository', 'git@github.com:acme/example.org.git');

desc('Upload project files');
task('deploy:update_code', function () {
    foreach([
        'config',
        'contao',
        'public/layout',
        'public/favicon.ico',
        'src',
        '.env',
        'composer.json',
        'composer.lock',
    ] as $src) {
        upload($src, '{{release_path}}/', ['options' => ['--recursive', '--relative']]);
    }
});
```

Instead of defining every file and folder in `upload()`, the `rsync` task can also be used. The `rsync` task implies an *exclude strategy* rather than an *include strategy*. An example and the `contao-rsync.php` recipe are at `nutshell-framework/deployer-recipes`.

### Provision web server

The document root of the server has to be set to `/public` of the project. The idea of Deployer is to provide updates with the shortest possible downtime, and to realize this, Deployer utilizes rolling symlink releases. Consequently, the document root of the vHost must be set to `/current/public` (or `/current/web` respectively). A full example for the document root might look like `/var/www/foobar/html/example.org/current/public`.

**Info note:** by default, Contao uses the `/public` folder of the project as the document root. If the Contao installation is still using the legacy `/web` folder as public directory, set it explicitly in the `composer.json` of the project:

```json
{
  "extra": {
    "public-dir": "web"
  }
}
```

### Add build-task to deployment

Additional build tasks tailored to the project can be added to the deployment process:

```php
// deploy.php

/* Your existing config */

// Task to build the assets, i.e., run `yarn run build` on the local machine
desc('Build assets')
task('encore:compile', function () {
    runLocally('yarn run build');
});

// Define that the assets should be generated before the project is going to be deployed
before('deploy', 'encore:compile');
```

### Finally: Deploy

Run `vendor/bin/dep deploy`.

### Tips

#### Custom recipes

One or many recipes can be used in a project, and logic can be extracted into own recipes. Collections of Deployer recipes named upstream:

- https://github.com/nutshell-framework/deployer-recipes
- https://github.com/terminal42/deployer-recipes/

#### Contao Manager

A task can be provided to download the Contao Manager on each deploy:

```php
// deploy.php

/* Your existing deploy.php */

before('deploy:publish', 'contao:manager:download');
// Optionally lock the Contao Manager if you don't use the UI
after('contao:manager:download', 'contao:manager:lock');
```

#### Symlink issues with OPCache / APCu

As Deployer uses a symlink for the document root, issues might occur with internal caches like OPCode Caching. To check what caches are in place, check the Symfony toolbar (lower right corner), which should show a green tick for OPCache.

For the caches being in place, this is an example to clear the caches:

```php
// deploy.php

// Add this recipe
require 'contrib/cachetool.php';

host('www.example.com')
    // Add this option, change {{hostname}} to the actual URL when the hostname does not match the URL.
    ->set('cachetool_args', '--web=SymfonyHttpClient --web-path=./{{public_path}} --web-url=https://{{hostname}}')
;

after('deploy:success', 'cachetool:clear:opcache');
// or
after('deploy:success', 'cachetool:clear:apcu');
```

#### Handle failed deployments

Deployer only activates the new build when the deployment is without errors. However, when a deployment fails, the deployment may be left in a locked state and the Contao installation in maintenance mode. The deployment can be unlocked automatically (to allow follow-up deployments) and the Contao maintenance mode disabled after failed deployments:

```php
// deploy.php

after('deploy:failed', 'deploy:unlock');
after('deploy:failed', 'contao:maintenance:disable');
```

## Create an installable theme

**Source:** https://docs.contao.org/5.x/manual/en/guides/manager-theme/

This guide explains how to build a theme archive that can be selected during a Contao Manager installation. It is not only relevant for theme providers: an own page structure, including extensions and layout, can be created and used during Manager installation.

### Theme Manager

The "Theme Manager" in the back end can export and import existing themes as a `.cto` file. However, this exported `.cto` is not suitable for use in the Contao Manager, as it requires further information.

### Theme Structure for the Manager

In addition to the actual `assets`, a theme for the Contao Manager requires a `theme.xml` file, the respective `composer.json` and an `SQL dump`. This data can be summarized as a `.zip` archive and then be used in the Contao Manager. As an orientation of the structure, the `.zip` archive of the "Contao Demo" (https://github.com/contao/contao-demo/tags) is helpful.

```bash
>files
>templates
>var/backups
composer.json
theme.xml
```

Each file and directory within the archive is imported into the Contao root directory (except for `theme.xml`). Therefore, a `config/config.yaml` with further settings, such as `contao.image.imagine_options.jpeg_quality: 95`, can also be added. Another example is the Isotope eCommerce Demo (https://github.com/isotope/isotope-demo).

#### Assets and the "theme.xml"

1. Obtain this data from the existing installation via the "Theme Manager" in the back end.
2. The exported `.cto` file is actually a `.zip` archive, so rename the file accordingly and then unzip it.
3. Afterwards the directories `files`, `templates` and the file `theme.xml` are present.

#### SQL-Dump

1. Create the current SQL dump of the theme installation via the backup command on the console or via the Contao Manager (`Maintenance - Database Migrations and Backups`). A normal PHPMyAdmin export would not be sufficient.

```bash
php vendor/bin/contao-console contao:backup:create
```

2. Then copy the `var/backups` directory with the current SQL dump into the unzipped directory above. Only one SQL dump may exist in this directory.

The SQL dump is always optional. Without it, only the files are installed.

**Tip:** the configuration options of the backup command can be used to exclude various database tables such as `tl_log`.

#### The "composer.json"

1. Copy the current `composer.json` of the theme installation into the unpacked directory. Optional information can be added to it (see the Contao Demo `composer.json` at https://github.com/contao/contao-demo/blob/5.3.x/composer.json).

The label `"type": "contao-theme"` is mandatory and necessary for the Contao Manager.

### Your Theme

The theme directory now contains all the necessary information. It can now be archived as a `.zip` file and used for a new installation via the Contao Manager. The directory itself must not be compressed, only the files.

**Info note:** other files such as a `README.md` or license details can easily be added.

## Module Listing

**Source:** https://docs.contao.org/5.x/manual/en/guides/module-listing/

This guide realises a list of members together with a map display via OpenStreetMap for a fictitious club site, using the front end module of type "Listing", a custom DCA field for geo-coordinates, and the leaflet.js framework.

It requires corresponding Contao members who can be assigned to one or more Contao member groups (for example "tournament riders" or "board"). These details are stored in the database table `tl_member` and can then be queried via the module of the type "listing".

**Note:** for list display of existing members the extension `friends-of-contao/contao-memberlist` could also be installed. By using the module "Listing" this can be implemented without any extension.

### Module type »Listing«

From any database table, records can be retrieved that can then be output to the front end using template files. The module realizes a comfortable input of simple SQL queries. The results are displayed by default, among other things to display a list (template: `list_default.html5`) with optional links to detail pages (template: `info_default.html5`).

The respective field names can be found in the database table `tl_member`. Without specifying a condition, all specified data records are listed in the "Fields" area. Set the following specifications in the module:

- **Table**: `tl_member`
- **Fields**: `firstname, lastname, email, postal, street, city`
- **Condition**: `disable != 1`
- **Items per page**: `0`

#### Condition

The condition `disable != 1` filters the result of the query so that only members declared as "active" are displayed (in the sense of: no deactivated members).

Member groups are listed in the database table `tl_member_group`. Assuming the group "board" is present here with an "id" of "2", the reference of the group membership of a member is made in the table `tl_member` via the data set `groups`. To limit the member list to all "active" members of the group "board", the following condition can be entered: `disable != 1 AND groups LIKE '%"2"%'`.

#### Template »list_default.html5«

The template `list_default.html5` is extensive, because it considers all eventualities of the representation in interaction with the module. For this example the template is simplified.

1. Create a new template `list_default_member.html5` in the template directory specified under "Themes" and then use this in the "Listing" module:

```html
// list_default_member.html5

<style>
.mod_listing div.memberitem {
  border: 1px solid #dadada;
	margin: 4px 4px;
	display: block;
}
.mod_listing div p {
	padding: 10px 10px;
	margin: 0;
}	
</style>

<div class="<?= $this->class ?> ce_table listing block"<?= $this->cssID ?><?php if ($this->style): ?> style="<?= $this->style ?>"<?php endif; ?>>

  <?php if ($this->headline): ?>
    <<?= $this->hl ?>><?= $this->headline ?></<?= $this->hl ?>>
  <?php endif; ?>


  <?php if ($this->searchable && $this->for && empty($this->tbody)): ?>
    <?= $this->no_results ?>
  <?php else: ?>
	  <?php foreach ($this->tbody as $class => $row): ?>
	    <div class="block memberitem <?= $class ?>"><p>
	  	  <a href="mailto:<?= $row['email']['raw'] ?>">
	  	  <?= $row['firstname']['content'] ?> <?= $row['lastname']['content'] ?></a>
		  
          <span><?= $row['street']['content'] ?> - 
		  <?= $row['postal']['content'] ?> <?= $row['city']['content'] ?></span>
		</p></div>
      <?php endforeach; ?>
  <?php endif; ?>

  <?= $this->pagination ?>
</div>
```

**Info note:** for simplicity the CSS information is entered directly in the template. Alternatively it could be stored as CSS assets.

### New field for geo-coordinates

For the map display, the corresponding geo-coordinates of the address in the form of latitude and longitude are required for each member.

1. If they do not already exist, create a new folder `contao/dca` in the Contao main directory with a file `tl_member.php`:

```php
// contao/dca/tl_member.php

use Contao\CoreBundle\DataContainer\PaletteManipulator;

$GLOBALS['TL_DCA']['tl_member']['fields']['myGeoData'] = [
    'label'       => ['Coordinates of the address', 'Latitude and longitude separated by commas.'],
    'inputType'   => 'text', 
    'eval'        => ['tl_class' => 'w50'],
    'sql'         => ['type' => 'string', 'length' => 255, 'notnull' => false],
];

PaletteManipulator::create()
    ->addLegend('Geo-Coordinates', 'address_legend', PaletteManipulator::POSITION_AFTER)
    ->addField('myGeoData', 'Geo-Coordinates', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_member')
;
```

2. For Contao to accept this information, update the "application cache" in the "System maintenance" section of the console or the Contao Manager.
3. Then call the Contao installation tool, or use the console:

```bash
vendor/bin/contao-console contao:migrate
```

The new field `myGeoData` is then created in the database table `tl_member`. In the Contao back end the field can now be used to enter the geo-coordinates of a member, in the form of "latitude,longitude".

**Info note:** each time the file `contao/dca/tl_member.php` is changed, the "application cache" must be updated again.

#### Determination of the geo-coordinates

The required coordinates can be found via Nominatim/Openstreetmap (https://nominatim.openstreetmap.org/) or Google Maps. For this example, the one-time determination and manual entry of the coordinates is reasonable for the new admission of a member. With a lot of data, one of the numerous Contao map extensions could be used to automatically determine the coordinates. Another alternative is the extension `netzmacht/contao-leaflet-geocode-widget`.

#### Extension »netzmacht/contao-leaflet-geocode-widget«

The extension provides two back end widgets for geocoding of addresses including the perimeter. Integration instructions are on the GitHub page (https://github.com/netzmacht/contao-leaflet-geocode-widget). After installing the extension, `contao/dca/tl_member.php` can be customized as follows:

```php
// contao/dca/tl_member.php

use Contao\CoreBundle\DataContainer\PaletteManipulator;

$GLOBALS['TL_DCA']['tl_member']['fields']['myGeoData'] = [
    'label'       => ['Coordinates of the address', 'Latitude and longitude separated by commas.'],
    'inputType'   => 'leaflet_geocode', 
    'eval'        => ['tl_class' => 'w50'],
    'sql'         => ['type' => 'string', 'length' => 255, 'notnull' => false],
];

PaletteManipulator::create()
    ->addLegend('Geo-Coordinates', 'address_legend', PaletteManipulator::POSITION_AFTER)
    ->addField('myGeoData', 'Geo-Coordinates', PaletteManipulator::POSITION_APPEND)
    ->applyToPalette('default', 'tl_member')
;
```

Instead of the previous text field, only the `inputType` is changed to `leaflet_geocode` according to the GitHub documentation. Afterwards, the Contao "application cache" needs to be updated. Even if the geo-coordinates of a member are still not determined automatically, they can now easily be obtained from within the Contao back end.

### Map display

The field `myGeoData` can be added in the module "Listing":

- **Fields**: `firstname, lastname, email, postal, street, city, myGeoData`

#### JavaScript Framework »leaflet.js«

The map is displayed via OpenStreetMap and the JavaScript framework leaflet.js is used to create the map. With the leaflet download (https://github.com/Leaflet/Leaflet/tags) the directory `dist` with the files `leaflet.js`, `leaflet.css` and `images/marker-icon.png` is found in the ZIP archive (currently v.1.7.1).

1. Based on `leaflet.js`, create a JavaScript file `myMemberLeafletMap.js` with the following content:

```js
// /files/myPathTo/myMemberLeafletMap.js

function createMemberMap(arrMemberData){

	const mapCssId = 'MYMEMBERMAP';
	const myMarkerIconURL = '/files/myPathTo/leaflet/images/marker-icon.png'; 
	
	const zoomDefault = 12;
	const zoomMin = 1;
	const zoomMax = 18;

	var myMarkerIcon = new L.icon({
	  iconUrl: myMarkerIconURL,
	  iconSize:     [25, 41],
	  iconAnchor:   [12, 41],
	  popupAnchor:  [0, -30]
	});

	var memberGroup = new L.featureGroup();
	
	for (var i = 0; i < arrMemberData.length; i++) {
		var current = arrMemberData[i];
		memberGroup.addLayer(L.marker(current.LatLong).bindPopup(current.markerPopupContent));
	}

	var mapProvider =
	new L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	  attribution: '&copy;<a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	});

	var map = new L.Map(mapCssId, {
	  minZoom: zoomMin,
	  maxZoom: zoomMax,
	  scrollWheelZoom: false,
	  fadeAnimation: false,
	  layers: [mapProvider, memberGroup]
	});

	var bounds = L.latLngBounds(memberGroup.getBounds());
	map.fitBounds(bounds, {padding: [10, 10]});
    
	map.on("resize", function(e){ 
     map.fitBounds(bounds, {padding: [10, 10]}); 
   });
}
```

2. Adjust the directory information on the marker symbol (`myMarkerIconURL`) accordingly. Via `mapCssId` the CSS ID for the HTML container is defined. The JavaScript function expects as argument an array with the corresponding information. This information is assigned to a group `memberGroup`, together with OpenStreetMap as map provider, for the purpose of displaying the map.
3. Copy these files into a public directory of the Contao installation below `files`.

**Info note:** jQuery still needs to be enabled in the page layout of the theme. The example refers to the standard leaflet marker icon `images/marker-icon.png`. To use a different, individual symbol, the specifications `iconSize`, `iconAnchor` and `popupAnchor` must also be adapted.

#### Template adjustments »list_default_member.html5«

The existing template `list_default_member.html5` is supplemented as follows:

```html
<!-- list_default_member.html5 -->

<?php
	$GLOBALS['TL_CSS'][] = '/files/myPathTo/leaflet.css|static';
	$GLOBALS['TL_JAVASCRIPT'][] = '/files/myPathTo/leaflet.js|static';
	$GLOBALS['TL_JAVASCRIPT'][] = '/files/myPathTo/myMemberLeafletMap.js|static';
?>

<style>
.mod_listing div.memberitem {
	border: 1px solid #dadada;
	margin: 4px 4px;
	display: block;
}
.mod_listing div p {
	padding: 10px 10px;
	margin: 0;
}	
</style>

<div class="<?= $this->class ?> ce_table listing block"<?= $this->cssID ?><?php if ($this->style): ?> style="<?= $this->style ?>"<?php endif; ?>>

<?php if ($this->headline): ?>
	<<?= $this->hl ?>><?= $this->headline ?></<?= $this->hl ?>>
<?php endif; ?>

<?php if ($this->searchable && $this->for && empty($this->tbody)): ?>
	<?= $this->no_results ?>
<?php else: ?>
	<div id="MYMEMBERMAP" class="block" style="height:40vh"></div>

	<?php $tmpMemberMapData = '' ?>
	<?php foreach ($this->tbody as $class => $row): ?>
		<div class="block memberitem <?= $class ?>"><p>
		  <a href="mailto:<?= $row['email']['raw'] ?>">
		  <?= $row['firstname']['content'] ?> <?= $row['lastname']['content'] ?></a>
		  <span><?= $row['street']['content'] ?> - 
		  <?= $row['postal']['content'] ?> <?= $row['city']['content'] ?></span>
		</p></div>

		<?php $tmpMemberMapData .= sprintf("{'markerPopupContent': '%s',  'LatLong': [%s]},", 
			$row['firstname']['content'].' '.$row['lastname']['content'], 
			$row['myGeoData']['content']);
		?>
	<?php endforeach; ?>
<?php endif; ?>

<script> 
	var arrMemberMapData = [<?= $tmpMemberMapData ?>];

	(function($){
		$(document).ready(function(){ createMemberMap(arrMemberMapData); });
	})(jQuery);
</script>  

<?= $this->pagination ?>
</div>
```

First the required CSS and JS files are referenced. Furthermore an HTML container with the CSS ID `MYMEMBERMAP` is defined for map display. In the PHP loop the required coordinates are collected via `tmpMemberMapData` and a JavaScript array is generated in order to call the function `createMemberMap(arrMemberMapData)`.

**Info note:** the HTML container for map display requires a CSS height specification, set inline here for simplicity.

**Note:** when the map is retrieved, communication between the browser and the OpenStreetMap server is initiated. This transmission must be observed in the GDPR or ePrivacy context.

#### Map display after confirmation

The creation and display of the map should only take place after confirmation by the user. For example, a picture of the map together with corresponding information can be displayed first. After the user confirms this declaration of consent, the actual map display is initiated.

1. Add a new CSS class `static` to the HTML container in the template together with the corresponding CSS definitions:

```html
...
<style>
.static {
	background-color: rgba(0,0,0,0.2);
}
.static-info {
	text-align: center;
	position: relative;
	display: block;
	top: 50%;
	transform: translateY(-50%);
}
.js-static-info__close {
	display: inline-block;
	margin: 10px 0 0 0;
	background: #ffffff;
	padding: 6px 6px;
	cursor: pointer;
}
</style>

<div id="MYMEMBERMAP" class="block static" style="height:40vh"></div>
...
```

Only a colour value is given here in the example; a background image could be used instead.

2. Replace the JavaScript call of the function as follows:

```JS
<script> 
var arrMemberMapData = [<?= $tmpMemberMapData ?>];

(function($){
	$(document).ready(function(){ 
		if (localStorage) {
			if (localStorage.getItem('MapHide') !== 'true') {
    			var info = 
    			'<div class="static-info"><div>Ja, ich möchte Karten von OpenStreetMap angezeigt bekommen.<br>' +
    			'Weitere Informationen finden Sie in unseren Datenschutzhinweisen.</div>' +
    			'<div class="js-static-info__close">Karte einblenden</div></div>';
    			$('#MYMEMBERMAP').prepend(info);
			} else {
  				$('#MYMEMBERMAP').removeClass('static');
  				createMemberMap(arrMemberMapData);
			}
		}

		$('.js-static-info__close').click(function(){
    		$(this).parents('.static-info').remove();
    		$('#MYMEMBERMAP').removeClass('static');

    		createMemberMap(arrMemberMapData);
    		localStorage.setItem('MapHide', 'true');
		});
	});
})(jQuery);
</script>
```

As long as there is no confirmation from the user, the "static" alternative is displayed. Otherwise the map is created and displayed. Instead of a cookie, the `localStorage` functionality of the browser is used (`sessionStorage` could also be used).

#### Useful leaflet plugins

- **Leaflet.fullscreen** (https://github.com/Leaflet/Leaflet.fullscreen): expands the map with a fullscreen view.
- **Leaflet.TileLayer.Grayscale** (https://github.com/Zverik/leaflet-grayscale): some map providers have grayscale tiles; with this plugin maps can be displayed in greyscale.
- **Leaflet.markercluster** (https://github.com/Leaflet/Leaflet.markercluster): with numerous markers, depending on the zoom level, several markers are clearly summarised and displayed.

## Using web fonts

**Source:** https://docs.contao.org/5.x/manual/en/guides/webfont/

This guide covers integrating web fonts into Contao, either via external Google hosting or via local hosting, and controlling load behaviour with the CSS `font-display` property.

### Commercial or Open Source?

Besides commercial service providers like Adobe Fonts or fonts.com there are Open Source alternatives available. With most commercial providers the web fonts are "rented" and hosted on their own servers; only few offer the web fonts for download. The most well known free offer is Google with Google Fonts. Alternatives are found on GitHub (adobe-fonts). With Open Source offers it should be checked that they contain special characters. Also, possibly only a few or even no further typefaces are available.

### File formats

For historical reasons there are different file formats such as `.eot`, `.ttf`, `.woff` or `.woff2`. In the meantime the formats `.woff` or `.woff2` can be used in current browser versions. To support older browsers, the other file formats can also be used.

### Contao Integration

The example uses the Google Font "Vollkorn", with the typefaces "Bold 700 italic" and "Semi-bold 600".

#### Via external Google hosting

1. Via Google Fonts, select the required font styles of the font "Vollkorn" and receive an "embed" instruction for integration, for example:

```html
<link href="https://fonts.googleapis.com/css2?family=Vollkorn:ital,wght@0,600;1,700&display=swap" rel="stylesheet">
```

2. Write this instruction in the "Expert Settings -> Additional `<head>`-Tags" within the Page Layouts of the theme. Google provides the information required by the respective browser and no further action is required.
3. The selected fonts can then be used in the CSS information:

```CSS
h1, h2 {
  font-family: 'Vollkorn', serif;
  font-style: italic;
  font-weight: 700;
}
```

**Info note:** in the Page layouts there may be direct input options for the Google web fonts. This option will no longer be available in future versions of Contao, so the described procedure is recommended.

**Warning:** the retrieval of the web fonts triggers a communication between the browser displaying the website and the Google server. In the process, data about the browser or the IP are also transmitted. This transmission is to be considered with the GDPR or ePrivacy. It is recommended to install the fonts via a local integration.

#### Local integration

Web fonts can also be integrated locally, via own hosting.

1. Obtain the respective files and place them in a publicly accessible directory of the Contao installation under `files`. In the case of Google Fonts a download option is offered, but this download includes only files in the `.ttf` format.
2. Web applications like Google Webfonts Helper (https://gwfh.mranftl.com/fonts) or Web Font Loader (https://webfontloader.altmann.de/) provide the Google web fonts in various file formats. Furthermore, depending on the selection, the appropriate CSS information via `@font-face` is supplied.
3. This CSS information must be added to the own CSS file. It does not matter whether CSS files are used directly or via preprocessors such as Sass/Less.
4. Then include the CSS file as an external stylesheet in the "Expert settings -> Stylesheets" within the page layout section of the theme.

**Note:** a post at https://webfontloader.altmann.de/about/#more clarifies the differences between the mentioned web applications.

**Info note:** the paths provided in `url()` regarding the web font files within the CSS `@font-face` directive are relative to the position of the CSS file. This depends on the directory structure.

Assuming the web font files have been copied into a directory `files/theme/fonts` and the CSS file is in the directory `files/theme/css`, the correct relative paths to the web font files would be:

```CSS
/* vollkorn-600 - latin */
@font-face {
  font-family: 'Vollkorn';
  font-style: normal;
  font-weight: 600;
  src: url('../fonts/vollkorn-v12-latin-600.eot');
  src: local(''),
       url('../fonts/vollkorn-v12-latin-600.eot?#iefix') format('embedded-opentype'),
       url('../fonts/vollkorn-v12-latin-600.woff2') format('woff2'),
       url('../fonts/vollkorn-v12-latin-600.woff') format('woff'),
       url('../fonts/vollkorn-v12-latin-600.ttf') format('truetype'),
       url('../fonts/vollkorn-v12-latin-600.svg#Vollkorn') format('svg');
}
```

**Note:** in the Page Layout, the "Combine Scripts" option can be activated. All CSS information of the selected internal and external CSS files is combined into a single new file and stored by Contao in the directory `assets/css`. Since the new CSS file is then located in `assets/css`, the paths to the web fonts must be adapted; Contao does this automatically during this process: `... url('../../files/theme/fonts/vollkorn-v12-latin-600.woff2') format('woff2'), ...`.

### The CSS "font-display" property

A web font file, if it is not already in the browser cache, must first be completely downloaded by the browser before it can be used. During page load the browser must react accordingly. Possibilities stated upstream: as long as a web font file is not completely available, the browser hides it and uses the web font after complete loading, the "Flash Of Invisible Text Effect (FOIT)"; or, if a longer loading time is required, a fallback font is used first.

The browser behaviour can be controlled via the CSS property `font-display`, which can be used within a CSS `@font-face` declaration with four values: `auto`, `swap`, `fallback` and `optional`.

The value `swap` is used in most cases and is also found in the Google Fonts embed instructions. Accordingly, the CSS information for local use can be extended:

```CSS
@font-face {
  font-display: swap;
...
}
```

## Front end filter implementation

**Source:** https://docs.contao.org/5.x/manual/en/guides/filter/

This guide presents four options for implementing an animated front end filter (for example for references, without reloading the website): with a dedicated extension, with Filterizr plus template adaptation, with a DCA manipulation, and with RockSolid Custom Elements. The contents to be filtered must first be assigned to appropriate categories, after which the presentation can be influenced via these categories.

### With an Extension

The extension `codefog/contao-elements-filter` can be used. More information is on the author's GitHub page (https://github.com/codefog/contao-elements-filter).

Pro: a Contao extension performs a special task, is mostly free of charge and can be easily installed. The actual technical implementation does not have to be dealt with. Editing is easily done using the well known Contao input options. Documentation, especially for free extensions, is usually done via the corresponding GitHub pages. Alternatively, support is available via the community in the Contao forum.

Contra: if Contao is updated or the PHP version changed, the extension might not yet be ready for this. In that case one has to rely on the author's modifications.

### Without extension

Known JavaScript solutions are Isotopes (https://isotope.metafizzy.co/) or MixItUp (https://github.com/patrickkunka/mixitup); in case of commercial use the purchase of licenses is necessary. This example uses the open source solution Filterizr (https://yiotis.net/filterizr/#/).

#### Use of »Filterizr«

The solution can be implemented either as jQuery Plugin or as Vanilla JS. The guide uses Vanilla JS.

1. After the download (https://github.com/giotiskl/filterizr/tags), the directory `dist` with the file `vanilla.filterizr.min.js` is found in the zip archive. Copy this file into a public directory of the Contao installation below `files`.
2. For the Filterizr script, the content to be filtered must be declared with the CSS class `filtr-item`. The category assignment is done via an HTML5 data attribute `data-category`. An exemplary HTML structure could look like the following and must be mapped within Contao:

```html
<ul>
  <li data-filter="all">All animals</li>
  <li data-filter="Dog">Dogs only</li>
  <li data-filter="Cat">Cats only</li>
</ul>

<div class="filter-container">

  <div class="filtr-item" data-category="Dog">
    <img src="sample1.jpg" />
  </div>
  <div class="filtr-item" data-category="Cat">
    <img src="sample2.jpg" />
  </div>

</div>

<script type="text/javascript" src="files/MyPathToFile/vanilla.filterizr.min.js"></script>
<script>const filterizr = new Filterizr('.filter-container');</script>
```

The above HTML structure can be created with Contao's own content elements: content elements of type "HTML" for the HTML blocks and one or more elements of type "Text" for the actual content. The implementation in the Contao back end is therefore:

1. Content element of type "HTML":

```html
<ul>
  <li data-filter="all">All animals</li>
  <li data-filter="Dog">Dogs only</li>
  <li data-filter="Cat">Cats only</li>
</ul>
```

2. Content element of type "HTML":

```html
<div class="filter-container">
```

3. One or more content element(s) of type "Text": enter the texts and photos as usual. In the section "Expert settings CSS-ID/Class" set the required CSS class `filtr-item`.

4. Content element of type "HTML":

```html
</div>

<script type="text/javascript" src="files/MyPathToFile/vanilla.filterizr.min.js"></script>
<script>const filterizr = new Filterizr('.filter-container');</script>
```

#### With template adaptation

The remaining piece is the assignment of the categories via the HTML5 data attribute. In the content element of type "Text" this input option is missing. It can be realized by using customized Contao templates: when certain conventionally defined specifications are entered in the "Expert settings CSS-ID/Class" section, these are to be output as HTML5 data attributes via the template. When entering `filtr-item DATA-dog` in the CSS class area, the following output is desired:

```html
...
<div class="ce_text filtr-item block" data-category="Dog">
...
```

1. Create two new templates based on `ce_text.html5` and `block_searchable.html5` in the template directory specified under "Themes", for example as `ce_text_filter.html5` and `block_searchable_filter.html5`, and use the new template `ce_text_filter.html5` in the content elements of type "text" to be filtered.

```html
// ce_text_filter.html5

<?php $this->extend('block_searchable_filter'); ?>

<?php $this->block('content'); ?>

  <?php if (!$this->addBefore): ?>
    <?= $this->text ?>
  <?php endif; ?>

  <?php if ($this->addImage): ?>
    <?php $this->insert('image', $this->arrData); ?>
  <?php endif; ?>

  <?php if ($this->addBefore): ?>
    <?= $this->text ?>
  <?php endif; ?>

<?php $this->endblock(); ?>
```

```html
// block_searchable_filter.html5

<?php
$strDelimiter = "DATA-";
$strPattern = '/'.$strDelimiter.'(.+?)\b/i';  
$strDataAttr = "data-category"; 
$strCSS = $this->class; 

if ( substr_count($strCSS, $strDelimiter) > 0 ) {

  preg_match_all($strPattern, $strCSS, $arrMatches, PREG_PATTERN_ORDER, 0);

  for( $i = 0; $i <= count($arrMatches); $i++) {
    $strCSS = str_replace($arrMatches[0][$i], "", $strCSS);          
    $arrMatchedValues[] = $arrMatches[1][$i];      
  }    
  $strData = $strDataAttr.'="'.rtrim(implode(", ", $arrMatchedValues), ", ").'"';
}
?>

<div class="<?= $strCSS ?> block"<?= $strData ?><?= $this->cssID ?><?php if ($this->style): ?> style="<?= $this->style ?>"<?php endif; ?>>

  <?php $this->block('headline'); ?>
    <?php if ($this->headline): ?>
      <<?= $this->hl ?>><?= $this->headline ?></<?= $this->hl ?>>
    <?php endif; ?>
  <?php $this->endblock(); ?>

  <?php $this->block('content'); ?>
  <?php $this->endblock(); ?>

</div>
```

**Tip:** the script expects the contents within an HTML block `<div class="filter-container">...</div>`. For a clearer back end display, the Contao accordion elements "Envelope start" and "Envelope end" could be used for other purposes; in the element "Envelope start" the CSS class `filter-container` is then used. Furthermore, for simplicity, the JavaScript references are entered directly in the content element; alternatively they could be stored as JavaScript Asset in the template.

Pro: no reliance on extensions and complete control over implementation and maintenance. For Contao updates, only possible changes to the core templates might have to be considered.

Contra: for template adjustments in this form, at least rudimentary PHP knowledge is required. The use of HTML5 data attributes is not obvious to editors and requires documentation.

#### Manipulation of »Data Container Arrays«

This example takes over the previous implementation via the content elements. For the input of the HTML5 data attributes, a new, additional input field is created for the content element of type "Text" and the Contao Data Container Array (DCA) is extended for this purpose. The Contao file `tl_content.php` and the corresponding database table `tl_content` is responsible for the content elements.

1. If not already there, create a new directory `contao/dca` in the Contao root directory with a file `tl_content.php`:

```php
// contao/dca/tl_content.php

use Contao\CoreBundle\DataContainer\PaletteManipulator;

$GLOBALS['TL_DCA']['tl_content']['fields']['myCustomDataAttributes'] = [
  'label'     => ['Data-Attribut', 'Set your Html Data-Attribut.'],
  'inputType' => 'keyValueWizard',
  'default'   => serialize([['key' => 'data-category']]),
  'eval'      => ['tl_class' => 'w50'],
  'exclude'   => true,
  'sql'       => "text NULL",
];

PaletteManipulator::create()
  ->addLegend('Settings Data-Attribut', 'expert_legend', PaletteManipulator::POSITION_AFTER)
  ->addField('myCustomDataAttributes', 'Settings Data-Attribut', PaletteManipulator::POSITION_APPEND)
  ->applyToPalette('text', 'tl_content')
;

```

2. In order for Contao to take over this information, update the "application cache" in the "System maintenance" section of the Contao Manager.
3. Then call the Contao installation tool. The tool recognizes the new field and offers to create it in the database table `tl_content`. Every time the file `contao/dca/tl_content.php` is changed this will be necessary again.

The content element of type "Text" now contains a new input field (as key/value pair) for the data attributes below the "Expert settings". For example specify `data-category` in the field "Key" and an entry `Dog` in the field "Value".

4. For the output on the website, adapt the template files again. Analogous to the previous example the two template files `ce_text_filter.html5` and `block_searchable_filter.html5` are used.

```html
// ce_text_filter.html5

<?php $this->extend('block_searchable_filter'); ?>

<?php $this->block('content'); ?>

  <?php if (!$this->addBefore): ?>
    <?= $this->text ?>
  <?php endif; ?>

  <?php if ($this->addImage): ?>
    <?php $this->insert('image', $this->arrData); ?>
  <?php endif; ?>

  <?php if ($this->addBefore): ?>
    <?= $this->text ?>
  <?php endif; ?>

<?php $this->endblock(); ?>
```

```html
// block_searchable_filter.html5

<?php if ($this->myCustomDataAttributes) {
  $dataAttributesString = "";
  $dataAttributes = \StringUtil::deserialize($this->myCustomDataAttributes); 
  $parsedDataAttributes = [];

  foreach ($dataAttributes as $index=>$dataAttribute) {
    $parsedDataAttributes[] = 'data-' . str_replace('data-', '', $dataAttribute['key']) 
    . '="' . $dataAttribute['value'] 
    . '"';
  }
  $dataAttributesString = implode(' ' , $parsedDataAttributes);
}
?>

<div class="<?= $this->class ?> block"<?= $this->cssID ?><?php if ($this->style): ?> style="<?= $this->style ?>"<?php endif; ?> <?= $dataAttributesString ?>>

  <?php $this->block('headline'); ?>
    <?php if ($this->headline): ?>
      <<?= $this->hl ?>><?= $this->headline ?></<?= $this->hl ?>>
    <?php endif; ?>
  <?php $this->endblock(); ?>

  <?php $this->block('content'); ?>
  <?php $this->endblock(); ?>

</div>
```

Pro: complete control over the implementation and maintenance. Editors can easily enter the required information in input fields.

Contra: rudimentary knowledge of PHP and the documented Contao DCA is required.

#### With »RockSolid Custom Elements«

`madeyourday/contao-rocksolid-custom-elements` (RSCE) is a Contao extension that allows creating individual content elements and front end modules with convenient input and output in Contao.

Pro: using three different extensions from different authors (for example a front end filter, an alternative content slider and a photo gallery) means more work for future Contao updates the more extensions are used. By using RSCE this is limited to one single extension while still allowing easy editing of all three within Contao. Furthermore, the extension is maintained and kept up to date by Martin Auswöger (@ausi, member of the Contao core team).

Contra: knowledge of the documented Contao DCA is necessary.

The RSCE extension is based on the existing Contao conventions. Only two files are needed, created in the specified template directory of the theme; they can then be edited and maintained within Contao. These files are a `.php` configuration file with Contao DCA information and a `.html5` template file for output.

Naming convention: the name of the template file must start with `rsce_`, and the configuration file must have the same name as the template plus the suffix `_config`. For example `rsce_my_filter.html5` and `rsce_my_filter_config.php`.

```php
// rsce_my_filter_config.php

return array(
  'label' => array('Filter-Element', 'Frontend-Filter Content'),
  'types' => array('content'),
  'contentCategory' => 'texts',
  'standardFields' => array('headline', 'text', 'image', 'cssID'),
  'wrapper' => array(
    'type' => 'none',
  ),
  'fields' => array(
  'description' => array(
    'label' => array('Data-Attribut', 'Specification of one or more HTML Data attribute(s)'),
    'inputType' => 'group',
  ),
  'data' => array(
    'label'     => ['Data-Attribut:', 'Attribut-Name / Attribut-Value'],
    'inputType' => 'keyValueWizard',
    'default'   => serialize([['key' => 'data-category']]),
    'eval'      => ['tl_class' => 'w50'],
    ),
  ),
);
```

```html
// rsce_my_filter.html5

<?php if ($this->data){

  $dataAttributesString = "";
  $dataAttributes = $this->data; 
  $parsedDataAttributes = [];

    foreach ($dataAttributes as $index=>$dataAttribute) {
      $parsedDataAttributes[] = 'data-' . str_replace('data-', '', $dataAttribute['key']) 
      . '="' . $dataAttribute['value'] 
      . '"';
    }
    $dataAttributesString = implode(' ' , $parsedDataAttributes);
}
?>

<div class="<?= $this->class ?> block" <?= $this->cssID ?> <?= $dataAttributesString ?>>
  <?php if ($this->headline): ?>
    <<?= $this->hl ?>><?= $this->headline ?></<?= $this->hl ?>>
  <?php endif; ?>

  <?php if ($this->addBefore): ?>
    <?= $this->text ?>
  <?php endif; ?>

  <?php if ($this->addImage): ?>
    <?php $this->insert('image', $this->arrData); ?>
  <?php endif; ?>

  <?php if (!$this->addBefore): ?>
    <?= $this->text ?>
  <?php endif; ?>
</div>
```

A new, own content element can then be chosen under the name "Filter-Element". This can be used for the content to be filtered in combination with the content elements of the type "HTML".

**Tip:** with the RSCE extension, own envelope elements could also be created and used instead of the previous content elements of type "HTML".

**Info note:** the extension "MetaModels" follows a similar approach and does not confront the user with a direct Contao DCA configuration. However, this extension goes far beyond the requirements necessary here, and the learning curve is accordingly higher.

### Conclusion

Contao offers many possibilities to meet requirements. The way of implementation is always a balance between comfort and later update effort. Especially for client-side solutions that are only based on the interaction of HTML, CSS and JavaScript, Contao provides a variety of solutions independent of existing extensions.

## Source

Distilled from the [Contao 5 user manual](https://docs.contao.org/5.x/manual/en/guides/), retrieved
2026-08-21:

- https://docs.contao.org/5.x/manual/en/guides/deployer/
- https://docs.contao.org/5.x/manual/en/guides/manager-theme/
- https://docs.contao.org/5.x/manual/en/guides/module-listing/
- https://docs.contao.org/5.x/manual/en/guides/webfont/
- https://docs.contao.org/5.x/manual/en/guides/filter/
