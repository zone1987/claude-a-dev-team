import Plugin from 'src/plugin-system/plugin.class';

export default class FfContentPlusPlugin extends Plugin {
    static options = {
        activeClass: 'is-active',
        selector: '.ff-content-plus-item',
    };

    init() {
        this._registerEvents();
    }

    _registerEvents() {
        this.el.addEventListener('click', this._onClick.bind(this));
    }

    _onClick(event) {
        event.preventDefault();
        this.el.classList.toggle(this.options.activeClass);
    }
}
