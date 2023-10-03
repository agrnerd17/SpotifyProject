//import ajax

// 2 const var's
const clientId = "24c1ee3495f44ae7ae83eccae3955650"
const code = undefined; 



//checks to see if there is a code
//if there is no code, user is redirected to authorization page
if (!code) {
    //add func to redirect the user, call from py file
    redirectToAuthCodeFlow(clientId);
} else {
    const accessToken = await getAccessToken(clientId, code);
    const profile = await fetchProfile(accessToken);
    populateUI(profile)
}

async function redirectToAuthCodeFlow(clientId) {
    //redirect to Spotify auth page
}

async function getAccessToken(clientId, code) {
    //gets access token for code
}

async function fetchProfile(token) {
    //call web API
}

function populateUI(profile) {
    //update UI with profile data
}