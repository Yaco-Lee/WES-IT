

document.addEventListener('DOMContentLoaded', function() {
    var currYear = (new Date()).getFullYear();
    var options = {
        maxDate: new Date(),
        yearRange: [1928, currYear],
        format: "yyyy-mm-dd",
    }
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, options);
  });