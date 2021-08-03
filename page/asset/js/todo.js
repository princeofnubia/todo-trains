// getting all required elements
const inputBox = document.querySelector(".inputField input");
const addBtn = document.querySelector(".inputField button");
const todoList = document.querySelector(".todoList");
const deleteAllBtn = document.querySelector(".footer button");
// onkeyup event
inputBox.onkeyup = ()=>{
  let userEnteredValue = inputBox.value; //getting user entered value
  if(userEnteredValue.trim() != 0){ //if the user value isn't only spaces
    addBtn.classList.add("active"); //active the add button
  }else{
    addBtn.classList.remove("active"); //unactive the add button
  }
}
showTasks(); //calling showTask function
// addBtn.onclick = ()=>{ //when user click on plus icon button
//   let userEnteredValue = inputBox.value; //getting input field value
//   let getLocalStorageData = localStorage.getItem("todo"); //getting localstorage
//   if(getLocalStorageData == null){ //if localstorage has no data
//     listArray = []; //create a blank array
//   }else{
//     listArray = JSON.parse(getLocalStorageData);  //transforming json string into a js object
//   }
//   listArray.push(userEnteredValue); //pushing or adding new value in array
//   localStorage.setItem("todo", JSON.stringify(listArray)); //transforming js object into a json string
//   showTasks(); //calling showTask function
//   addBtn.classList.remove("active"); //unactive the add button once the task added
// }
let postData;
addBtn.onclick = ()=>{ //when user click on plus icon button
  let userEnteredValue = inputBox.value; //getting input field value
  postData = {
    task_name: userEnteredValue,
    user: 1,
    task_status: 'todo',
    is_archived: false,
    scheduled_on: new Date().now()
  }
}
function showTasks(){
  let getLocalStorageData = localStorage.getItem("todo");
  if(getLocalStorageData == null){
    listArray = [];
  }else{
    listArray = JSON.parse(getLocalStorageData); 
  }
  const pendingTasksNumb = document.querySelector(".pendingTasks");
  pendingTasksNumb.textContent = listArray.length; //passing the array length in pendingtask
  if(listArray.length > 0){ //if array length is greater than 0
    deleteAllBtn.classList.add("active"); //active the delete button
  }else{
    deleteAllBtn.classList.remove("active"); //unactive the delete button
  }
  let newLiTag = "";
  listArray.forEach((element, index) => {
    newLiTag += `<ul class="todoListBody"><li> ${index} </li><li> ${element} </li><li>201011 </li> <li>progress </li> <span class="icon" onclick="deleteTask(${index})"><i class="fas fa-trash"></i></span></ul>`;
  });
  todoList.innerHTML = newLiTag; //adding new li tag inside ul tag
  inputBox.value = ""; //once task added leave the input field blank
}
// delete task function
function deleteTask(index){
  let getLocalStorageData = localStorage.getItem("todo");
  listArray = JSON.parse(getLocalStorageData);
  listArray.splice(index, 1); //delete or remove the li
  localStorage.setItem("todo", JSON.stringify(listArray));
  showTasks(); //call the showTasks function
}
// delete all tasks function
deleteAllBtn.onclick = ()=>{
  listArray = []; //empty the array
  localStorage.setItem("todo", JSON.stringify(listArray)); //set the item in localstorage
  showTasks(); //call the showTasks function
}

function fetchData() {
  window.fetch('http://127.0.0.1:8000/api/v1/todo/getTodos', {credentials: 'omit'}).then(data => {
    return data.json()
  }, err => console.log("there was an error", err)).then(data => {
    const pendingTasksNumb = document.querySelector(".pendingTasks");
    pendingTasksNumb.textContent = data.length; //passing the array length in pendingtask
    if(data.length > 0){ //if array length is greater than 0
      deleteAllBtn.classList.add("active"); //active the delete button
    }else{
      deleteAllBtn.classList.remove("active"); //unactive the delete button
    }
    let newLiTag = "";
    for (const key in data) {
      let index = 1
      if (data.hasOwnProperty(key)) {
        const element = data[key];
        newLiTag += `<ul class="todoListBody"><li> ${key} </li><li> ${element.task_name} </li><li>201011 </li> <li>progress </li> <span class="icon" onclick="deleteTask(${index})"><i class="fas fa-trash"></i></span></ul>`;
      }
    }
    todoList.innerHTML = newLiTag;
  })
}

fetchData()

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
     'Content-Type': 'application/json'
      //'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

postData('http://127.0.0.1:8000/api/v1/todo/createTodo', postData)
  .then(data => {
    console.log(data); // JSON data parsed by `data.json()` call
  });