// გავაზიარეთ მონაცემთა ბაზა:
let students = JSON.parse(localStorage.getItem('students')) || [
  { name: "მარი გვილავა", motherName: "ნათია ჯანაშა", facebook: "https://www.facebook.com/natialia1988?locale=ka_GE", age: 18, groupLeader: "ლუკა აკოფიანი" },
  { name: "გიორგი მჭედლიშვილი", motherName: "მარიამ შენგელია", facebook: "https://www.facebook.com/mari.shengelia.5454?locale=ka_GE", age: 19, groupLeader: "ლუკა აკოფიანი" },
];

// გაზიარების ფუქნცია რომ შევინახოტ ადამიანის ინფო
function saveStudents() {
  localStorage.setItem('students', JSON.stringify(students));
}

// რომელ გვერძე ვართ რომ გავარკვიოთ
function getCurrentPage() {
  const path = window.location.pathname;
  if (path.includes('moderator.html')) return 'moderator';
  if (path.includes('viewer.html')) return 'viewer';
  return 'index';
}

// sign in  ფეიჯის კოდი 
function handleSignIn() {
  let form = document.getElementById("signInForm");
  if (form) {
      form.addEventListener("submit", function(event) {
          event.preventDefault();
          const username = form.elements.username.value;
          const password = form.elements.password.value;
          const role = form.elements.role.value;

          if (username && password) {
              if (role === "viewer") {
                  window.location.href = 'viewer.html';
              } else if (role === 'moderator') {
                  window.location.href = 'moderator.html';
              }
          } else {
              alert("Please enter a username and password.");
          }
      });
  }
}

// მოდერატორ view კოდი
function handleModeratorPage() {
  function renderModeratorTable() {
      const tableBody = document.getElementById('studentTableBody');
      if (!tableBody) return;
      
      tableBody.innerHTML = '';

      students.forEach((student, index) => {
          const row = tableBody.insertRow();
          Object.keys(student).forEach(key => {
              const cell = row.insertCell();
              const input = document.createElement('input');
              input.type = 'text';
              input.value = student[key];
              input.addEventListener('change', (e) => {
                  students[index][key] = e.target.value;
                  saveStudents();
              });
              cell.appendChild(input);
          });

          const actionsCell = row.insertCell();
          const deleteBtn = document.createElement('button');
          deleteBtn.textContent = 'Delete';
          deleteBtn.addEventListener('click', () => {
              students.splice(index, 1);
              saveStudents();
              renderModeratorTable();
          });
          actionsCell.appendChild(deleteBtn);
      });
  }

  const addStudentBtn = document.getElementById('addStudentBtn');
  if (addStudentBtn) {
      addStudentBtn.addEventListener('click', () => {
          const newStudent = {
              name: prompt("Enter student name:"),
              motherName: prompt("Enter mother's name:"),
              facebook: prompt("Enter Facebook account:"),
              age: prompt("Enter age:"),
              groupLeader: prompt("Enter group leader:")
          };

          if (Object.values(newStudent).every(value => value !== null && value !== "")) {
              students.push(newStudent);
              saveStudents();
              renderModeratorTable();
          } else {
              alert("All fields must be filled. Student not added.");
          }
      });
  }

  renderModeratorTable();
}

// viewer  კოდი
function handleViewerPage() {
  function renderViewerTable() {
      const tableBody = document.getElementById('studentTableBody');
      if (!tableBody) return;
      
      tableBody.innerHTML = '';

      students.forEach(student => {
          const row = tableBody.insertRow();
          Object.values(student).forEach(value => {
              const cell = row.insertCell();
              cell.textContent = value;
          });
      });
  }

  renderViewerTable();
}

// მთავარი ფუნქცია რომ არ აირიოს კოდი და იმუშვონ ერთად ( მოვიძიე სხვანაირად ვერვქენი ;დ )
document.addEventListener('DOMContentLoaded', function() {
  const currentPage = getCurrentPage();
  
  switch(currentPage) {
      case 'index':
          handleSignIn();
          break;
      case 'moderator':
          handleModeratorPage();
          break;
      case 'viewer':
          handleViewerPage();
          break;
  }
});