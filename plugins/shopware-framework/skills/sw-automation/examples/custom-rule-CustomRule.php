<?php declare(strict_types=1);

namespace FfContentPlus\Core\Rule;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Rule\Rule;
use Shopware\Core\Framework\Rule\RuleConfig;
use Shopware\Core\Framework\Rule\RuleConstraints;
use Shopware\Core\Framework\Rule\RuleScope;

/**
 * @class FfContentPlusCustomRule
 * @package FfContentPlus\Core\Rule
 */
#[Package('custom-plugins')]
class FfContentPlusCustomRule extends Rule
{
    /**
     * @var string
     */
    final public const RULE_NAME = 'ff_content_plus_custom_rule';

    /**
     * @var float
     */
    protected float $amount = 0.0;

    /**
     * @var string
     */
    protected string $operator = self::OPERATOR_GTE;

    /**
     * @param RuleScope $scope
     * @return bool
     */
    public function match(RuleScope $scope): bool
    {
        // Implement matching logic
        return false;
    }

    /**
     * @return array<string, array<mixed>>
     */
    public function getConstraints(): array
    {
        return [
            'amount' => RuleConstraints::float(),
            'operator' => RuleConstraints::numericOperators(),
        ];
    }

    /**
     * @return RuleConfig
     */
    public function getConfig(): RuleConfig
    {
        return (new RuleConfig())
            ->operatorSet(RuleConfig::OPERATOR_SET_NUMBER)
            ->numberField('amount');
    }
}
