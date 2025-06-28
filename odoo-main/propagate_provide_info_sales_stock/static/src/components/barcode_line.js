/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import BarcodePickingModel from '@stock_barcode/models/barcode_picking_model';

patch(BarcodePickingModel.prototype, {
    setup() {
        super.setup(...arguments);
    },

    setData(data) {
        super.setData(...arguments);
        const stockPicking = data.data.records?.['stock.picking']?.[0];
        
        if (stockPicking) {
            this.shippingGuide = stockPicking.shipping_guide;
            this.purchaseOrderName = stockPicking.purchase_order_name;
        }
    },
});