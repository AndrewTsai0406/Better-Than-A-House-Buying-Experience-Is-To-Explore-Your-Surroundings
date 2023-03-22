var map;
var markers = {}
var infowindow;
var delayIn = 500;
// build content for view after clicking the location marker
function content(id, address) {
    return `<h3>No. ${id} Building</h3> <br>Address: ${address} <br><a href="https://maps.google.com/?q=${address}" class="link-secondary" target="_blank">Check the area on Google Map</a>`;
};

setTimeout(function initMap() {
    var data = JSON.parse(document.getElementById('radial').textContent);
    console.log(data)
    var data_1 = {lat: data[0]['lat'], lng: data[0]['lng']};
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: data_1	//the center point
    });

    infowindow = new google.maps.InfoWindow();
    // loop for all data
    for (var n = 0 ; n < data.length ; n++){
        addMarker(data[n]);
    }

    var a = -1;
    // add single marker
    function addMarker(data) {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(data['lat'], data['lng']),
            map: map,
            title: data['address']
        });
        markers[data['id']] = marker;
        // add click function
        google.maps.event.addListener(marker, "click", function() {
            infowindow.setContent(content(data['id'],data['address']));
            // use this to do open and close job
            a = a * -1;
            if(a > 0){
                infowindow.open(map, marker);
            }else{
                infowindow.close();
            }
        });

    };
    

  
}  , delayIn);


function centerLocation(id){
    // console.log(markers[id]);
    map.setCenter(markers[id].position);
    infowindow.setContent(content(id,markers[id].title));
    infowindow.open(map, markers[id]);
}

function updateCenter(marker){
    map.setCenter(marker.getPosition());
}

function typeSelected(value){
    if(value == 1){
        document.getElementById('total_floor_label').classList.remove("d-none");
        document.getElementById('total_floor_min').classList.remove("d-none");
        document.getElementById('total_floor_to').classList.remove("d-none");
        document.getElementById('total_floor_max').classList.remove("d-none");

        document.getElementById('floor_label').classList.add("d-none");
        document.getElementById('floor_min').classList.add("d-none");
        document.getElementById('floor_to').classList.add("d-none");
        document.getElementById('floor_max').classList.add("d-none");
    }else{
        document.getElementById('total_floor_label').classList.add("d-none");
        document.getElementById('total_floor_min').classList.add("d-none");
        document.getElementById('total_floor_to').classList.add("d-none");
        document.getElementById('total_floor_max').classList.add("d-none");

        document.getElementById('floor_label').classList.remove("d-none");
        document.getElementById('floor_min').classList.remove("d-none");
        document.getElementById('floor_to').classList.remove("d-none");
        document.getElementById('floor_max').classList.remove("d-none");
    }
}
