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
    fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/account", requestOptions)
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

var get_account = async (account_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var accountdata = fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/account?account_id=" + account_id, requestOptions)
        .then(response => response.json())
        .then(data => { return data.body })
        .catch(function (error) {
            console.log(error)
        });
    return await accountdata;
}

async function digestmessage(message) {
    const msgUint8 = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest("SHA-256", msgUint8);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
    return await hashHex;
}

var createaccount = document.querySelectorAll("input[value = S]")[0];

createaccount.addEventListener('click', () => {
    var formUsername = document.getElementById("newUsername");
    var formPostcode = document.getElementById("newPostcode");
    var formHouseNumber = document.getElementById("newHouseNumber");
    var formStreet = document.getElementById("newStreet");
    var formDietaryRequirement = document.getElementById("newDietaryRequirement");
    if (
        (formUsername.value == null || formUsername.value == "" ||
            formPostcode.value == "" || formPostcode.value == null ||
            formHouseNumber.value == null ||
            formHouseNumber.value == "" || formStreet.value == null ||
            formStreet.value == "" || formDietaryRequirement.value == null ||
            formDietaryRequirement.value == "")
    ) {
        alert("Fill out everything. Put None for dietary requirements if you have none.");
    }
    else {
        post_create_account(formUsername.value, "password", formPostcode.value, formHouseNumber.value, formStreet.value, formDietaryRequirement.value)
        // window.location.href = "main_page.html"
    }
});

var login = document.getElementById("login")

login.addEventListener('click', () => {
    var formUsername = document.getElementById("Username");
    if (
        (formUsername.value == null || formUsername.value == "")
    ) {
        alert("Enter Username.");
    }
    else {
        get_account(digestmessage(formUsername.value));
        if (accountdata == null) {
            alert("There is no such account.");
        } else {
            window.location.href = "main_page.html"
        }
    }
});