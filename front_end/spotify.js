var post_playlist_generate = (playlist_id, spotify_name, song_count, danceability) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Access-Control-Allow-Origin", "*")
    myHeaders.append("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
    myHeaders.append("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")
    var raw = JSON.stringify({ "playlist_id": playlist_id, "spotify_name": spotify_name, "song_count": song_count, "danceability": danceability });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow',
        mode: "no-cors"
    };
    fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/spotify_playlist_generate", requestOptions)
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
    myHeaders.append("Access-Control-Allow-Origin", "*")
    myHeaders.append("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
    myHeaders.append("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")
    var raw = JSON.stringify({ "playlist_id": playlist_id, "spotify_name": spotify_name, "choice": choice, "results": results });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        body: raw,
        redirect: 'follow',
        mode: "no-cors"
    };
    fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/spotify_playlist_search_add", requestOptions)
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
    myHeaders.append("Access-Control-Allow-Origin", "*")
    myHeaders.append("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
    myHeaders.append("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With")
    var raw = JSON.stringify({ "playlist_name": playlist_id, "spotify_username": spotify_name });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow',
        mode: "no-cors"
    };
    fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/spotify_playlist_create", requestOptions)
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

var get_search_string = async (search_string) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "search_string": search_string });
    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
    var messagedata = fetch("https://cwfusu2ly0.execute-api.eu-west-2.amazonaws.com/Prod/spotify_search?search_string=" + search_string, requestOptions)
        .then(response => { return response.json() })
        .catch(function (error) {
            console.log(error)
        });
    return await messagedata;
}

console.log(await get_search_string("Tesselate"))
console.log(await post_create_playlist("PlaylistTest2", "lhollister03"))
console.log(await post_playlist_generate("2", "GenerationTest2", 10, 0.9))