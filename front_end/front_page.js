var post_create_account = (username, password, postcode, house_number, street, dietary_info) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "username": username, "password": password, "postcode": postcode, "house_number": house_number, "street": street, "dietary_info": dietary_info });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    fetch("", requestOptions)
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Server response wasn\'t OK');
            }
        })
        .then((data) => {
            return data.statusCode;
        });
}

submit.addEventListener('click', (formFront, formBack) => {
    formUsername = document.getElementById("newUsername");
    formPostcode = document.getElementById("newPostcode");
    formHouseNumber = document.getElementById("newHouseNumber");
    formStreet = document.getElementById("newStreet");
    formDietaryRequuirement = document.getElementById("newDietaryRequuirement");
    if (
        (formUsername.value == null || formUsername.value == "", formBack.value == null ||
            formPostcode.value == "", formPostcode.value == null ||
            formHouseNumber.value == null ||
            formHouseNumber.value == "" || formStreet.value == null ||
            formStreet.value == "" || formDietaryRequuirement.value == null ||
            formDietaryRequuirement.value == "")
    ) {
        alert("Fill out everything. Put None for dietary requirements if you have none.");
    }
    else (
        post_create_account(formUsername.value, formPostcode.value, formHouseNumber.value, formStreet.value, formDietaryRequuirement.value)
    )
});