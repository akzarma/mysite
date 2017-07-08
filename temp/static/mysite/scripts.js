/**
 * Created by Akshay on 08-07-2017.
 */

function fileSizeValidate() {
    //alert("here");
    var profilePicture = document.getElementById("id_doc_profile_pic");
    var jee = document.getElementById("id_doc_jee_marksheet");
    var tenth = document.getElementById("id_doc_tenth_marksheet");
    var twelfth = document.getElementById("id_doc_twelfth_marksheet");

    //alert(element.name);
    var size1 = profilePicture.files[0].size;
    var size2 = jee.files[0].size;
    var size3 = tenth.files[0].size;
    var size4 = twelfth.files[0].size;
    var max_size = 5 * 1024 * 1024;
    //alert(element.files[0].size);
    if (size1 > max_size) {
        alert((Math.round(size1 / 1024 / 1024)).toString() + " MB. Profile Picture size too big!\nShould be smaller than 5MB");
        return false;
    }
    if (size2 > max_size) {
        alert((Math.round(size2 / 1024 / 1024)).toString() + " MB. JEE Marksheet size too big!\nShould be smaller than 5MB");
        return false;
    }
    if (size3 > max_size) {
        alert((Math.round(size3 / 1024 / 1024)).toString() + " MB. 10th Marksheet size too big!\nShould be smaller than 5MB");
        return false;
    }
    if (size4 > max_size) {
        alert((Math.round(size4 / 1024 / 1024)).toString() + " MB. 12th Marksheet size too big!\nShould be smaller than 5MB");
        return false;
    }
    else {
        return true;
    }
}
function successMsg() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar")

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function () {
        x.className = x.className.replace("show", "");
    }, 3000);
}
