var post_create_account = (event_id, account_ids, carpooler_id = null) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_id": event_id, "account_ids": account_ids, "carpooler_id": carpooler_id });
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

var post_create_event = (event_name, account_id, address, date, arrival_time, leaving_time) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_name": event_name, "account_id": account_id, "address": address, "date": date, "street": street, "arrival_time": arrival_time, "leaving_time": leaving_time });
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

var post_good_contribution = (event_name, account_id, reason, money) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_name": event_name, "account_id": account_id, "reason": reason, "money": money });
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

var post_money_contribution = (event_name, account_id, money) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_name": event_name, "account_id": account_id, "money": money });
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

var post_money_withdrawal = (event_name, account_id, money) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_name": event_name, "account_id": account_id, "money": money });
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

var post_create_account = (account_id, event_id, text) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "account_id": account_id, "event_id": event_id, "text": text });
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

var post_playlist_generate = (playlist_id, spotify_name, song_count, danceability) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "playlist_id": playlist_id, "spotify_name": spotify_name, "song_count": song_count, "danceability": danceability });
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

var post_playlist_search = (playlist_id, spotify_name, choice, results) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "playlist_id": playlist_id, "spotify_name": spotify_name, "choice": choice, "results": results });
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

var post_create_playlist = (playlist_id, spotify_name) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "playlist_id": playlist_id, "spotify_name": spotify_name });
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

var get_event = async (event_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_id": event_id });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    var eventdata = fetch("", requestOptions)
        .then(response => response.json())
        .then(data => { return data.body })
        .catch(function (error) {
            console.log(error)
        });
    return await eventdata;
}

var get_money_split = async (event_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_id": event_id });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    var moneydata = fetch("", requestOptions)
        .then(response => response.json())
        .then(data => { return data.body })
        .catch(function (error) {
            console.log(error)
        });
    return await moneydata;
}

var get_messages = async (event_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "event_id": event_id });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    var messagedata = fetch("", requestOptions)
        .then(response => response.json())
        .then(data => { return data.body })
        .catch(function (error) {
            console.log(error)
        });
    return await messagedata;
}

var get_search_string = async (search_string) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "search_string": search_string });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    var messagedata = fetch("", requestOptions)
        .then(response => response.json())
        .then(data => { return data.body })
        .catch(function (error) {
            console.log(error)
        });
    return await messagedata;
}