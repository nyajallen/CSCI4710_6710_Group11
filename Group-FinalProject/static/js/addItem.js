const loadFile = function (event) {
    const image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

function submit_handler() {
    let x = 1;
    if(x === 1) {
        $('#itemModal').modal('show');
        event.preventDefault();
    }
}

