$( document ).ready(function() {
const workoutList = ['Go for a run', 'Arms & Chest', 'Leg Day', 'Core'];

$('#jsButton').click(generateString);
function generateString(){
        $('#text').text(workoutList[generateText()]);
}
function generateText(){
        return Math.floor(Math.random() * workoutList.length)
}
});