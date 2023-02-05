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

var get_account = async (account_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "account_id": account_id });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    var accountdata = fetch("", requestOptions)
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

createaccount = document.getElementById("createaccount")

createaccount.addEventListener('click', () => {
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

login = document.getElementById("login")

login.addEventListener('click', () => {
    formUsername = document.getElementById("Username");
    if (
        (formUsername.value == null || formUsername.value == "", formBack.value == null)
    ) {
        alert("Enter Username.");
    }
    else {
        get_account(digestmessage(formUsername.value));
        if (accountdata == null) {
            alert("There is no such account.");
        }
    }
});