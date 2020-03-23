function cycle_display() {
    if (document.getElementById("cycle_display").innerHTML == 'Photos'){
        return document.getElementById("cycle_display").innerHTM = 'Businesses'
    }
    if (document.getElementById("cycle_display").innerHTML == 'Businesses'){
        return document.getElementById("cycle_display").innerHTM = 'Photos';
    }
}
