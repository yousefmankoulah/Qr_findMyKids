
//printing function
var myApp = new function () {
    this.printDiv = function () {
        // Store DIV contents in the variable.
        var img = document.getElementById('parent');
        
        // Create a window object.
        var win = window.open('', '', 'height=800,width=800'); // Open the window. Its a popup window.
        win.document.write(img.outerHTML);     // Write contents in the new window.
        win.document.close();
    }
}


