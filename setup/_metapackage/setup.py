import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-financial-tools",
    description="Meta package for oca-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_asset_batch_compute>=15.0dev,<15.1dev',
        'odoo-addon-account_asset_compute_batch>=15.0dev,<15.1dev',
        'odoo-addon-account_asset_low_value>=15.0dev,<15.1dev',
        'odoo-addon-account_asset_management>=15.0dev,<15.1dev',
        'odoo-addon-account_asset_management_menu>=15.0dev,<15.1dev',
        'odoo-addon-account_asset_number>=15.0dev,<15.1dev',
        'odoo-addon-account_asset_transfer>=15.0dev,<15.1dev',
        'odoo-addon-account_balance_line>=15.0dev,<15.1dev',
        'odoo-addon-account_chart_update>=15.0dev,<15.1dev',
        'odoo-addon-account_chart_update_l10n_eu_oss>=15.0dev,<15.1dev',
        'odoo-addon-account_chart_update_l10n_eu_oss_oca>=15.0dev,<15.1dev',
        'odoo-addon-account_check_deposit>=15.0dev,<15.1dev',
        'odoo-addon-account_cost_center>=15.0dev,<15.1dev',
        'odoo-addon-account_fiscal_month>=15.0dev,<15.1dev',
        'odoo-addon-account_fiscal_position_vat_check>=15.0dev,<15.1dev',
        'odoo-addon-account_fiscal_year>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_constraint_chronology>=15.0dev,<15.1dev',
        'odoo-addon-account_journal_general_sequence>=15.0dev,<15.1dev',
        'odoo-addon-account_journal_lock_date>=15.0dev,<15.1dev',
        'odoo-addon-account_loan>=15.0dev,<15.1dev',
        'odoo-addon-account_lock_date_update>=15.0dev,<15.1dev',
        'odoo-addon-account_lock_to_date>=15.0dev,<15.1dev',
        'odoo-addon-account_maturity_date_default>=15.0dev,<15.1dev',
        'odoo-addon-account_move_budget>=15.0dev,<15.1dev',
        'odoo-addon-account_move_fiscal_month>=15.0dev,<15.1dev',
        'odoo-addon-account_move_fiscal_year>=15.0dev,<15.1dev',
        'odoo-addon-account_move_force_removal>=15.0dev,<15.1dev',
        'odoo-addon-account_move_line_menu>=15.0dev,<15.1dev',
        'odoo-addon-account_move_line_purchase_info>=15.0dev,<15.1dev',
        'odoo-addon-account_move_line_residual>=15.0dev,<15.1dev',
        'odoo-addon-account_move_line_sale_info>=15.0dev,<15.1dev',
        'odoo-addon-account_move_line_tax_editable>=15.0dev,<15.1dev',
        'odoo-addon-account_move_name_sequence>=15.0dev,<15.1dev',
        'odoo-addon-account_move_print>=15.0dev,<15.1dev',
        'odoo-addon-account_move_template>=15.0dev,<15.1dev',
        'odoo-addon-account_move_total_by_account_internal_group>=15.0dev,<15.1dev',
        'odoo-addon-account_netting>=15.0dev,<15.1dev',
        'odoo-addon-account_sequence_option>=15.0dev,<15.1dev',
        'odoo-addon-account_spread_cost_revenue>=15.0dev,<15.1dev',
        'odoo-addon-account_usability>=15.0dev,<15.1dev',
        'odoo-addon-base_vat_optional_vies>=15.0dev,<15.1dev',
        'odoo-addon-product_category_tax>=15.0dev,<15.1dev',
        'odoo-addon-stock_account_no_auto_reconcile>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
