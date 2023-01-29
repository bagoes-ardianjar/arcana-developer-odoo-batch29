odoo.define('khaikal_perpustakaan.sheet', function (require){
"use strict";

// require original module JS
var timesheet = require('hr_timesheet_sheet.sheet');

// Extend widget
timesheet.WeeklyTimesheet.include({
    // ....
    // your code to override here    
    // ....
});
})