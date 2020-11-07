let number = 0


function addOne() {
    let count = document.getElementById('count');
    number++;
    count.textContent = number
    let status = document.getElementById('status')
    let goal = document.getElementById('goal').value
    console.log(goal)
    if ( number == 0) {
        status.textContent = 'Not started yet'
        console.log(number, goal)
    }
    else if (number < Number(goal)) {
        status.textContent = 'Pending'
    }
    else if (number == goal) {
        status.textContent = 'Completed!'
        console.log(number, goal)
    }
    else {
        status.textContent = "Overachieved!"
        console.log(number, goal)
    }
}
