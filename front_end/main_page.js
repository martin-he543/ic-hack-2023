var post_create_event = (event_name, account_id, address, date, arrival_time, leaving_time) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_name": event_name, "account_id": account_id, "address": address, "date": date, "arrival_time": arrival_time, "leaving_time": leaving_time });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/event", requestOptions)
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

async function digestmessage(message) {
    const msgUint8 = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest("SHA-256", msgUint8);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
    return await hashHex;
}

async function get_user() {
    //get username
    var username = ""
    return await digestmessage(username)
}

var createevent = document.getElementById("createEvent")

createevent.addEventListener('click', () => {
    var formEventName = document.getElementById("newEventName");
    var formPostcode = document.getElementById("newPostcode");
    var formHouseNumber = document.getElementById("newHouseNumber");
    var formStreet = document.getElementById("newStreet");
    var formDate = document.getElementById("newDate");
    var formArrivalTime = document.getElementById("newArrivalTime");
    var formLeavingTime = document.getElementById("newLeavingTime");
    var address = {
        "postcode": formPostcode.value,
        "street": formStreet.value,
        "house_number": formHouseNumber.value
    }
    if (
        (formEventName.value == null || formEventName.value == "" ||
            formPostcode.value == "" || formPostcode.value == null ||
            formHouseNumber.value == null ||
            formHouseNumber.value == "" || formStreet.value == null ||
            formStreet.value == "" || formDate.value == null ||
            formDate.value == "" || formArrivalTime.value == null ||
            formArrivalTime.value == "" || formLeavingTime.value == null ||
            formLeavingTime.value == "")
    ) {
        alert("Fill out everything.");
    }
    else {
        post_create_event(formEventName.value, get_user(), address, formDate.value, formArrivalTime.value, formLeavingTime.value)
    }
});