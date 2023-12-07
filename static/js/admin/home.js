window.onload = getData()

var roles
var users

function getData() {
    getUsersList()
    getRolesList()
}

function getRolesList() {
    $.ajax({
        url: "/secure_api/roles",
        type: 'GET',
        success: function(data) {
            roles = data
        },
        error: function(error) {
            console.error(error)
        },
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
    });
}

function getUsersList() {
    $.ajax({
        url: "/secure_api/users",
        type: 'GET',
        success: function(data) {
            users = data
            setTableData(data)
        },
        error: function(error) {
            console.error(error)
        },
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
    });
}

function setRoleDialog(roles, userId) {
    const dialogSelect = document.getElementById("roles-select")
    
    dialogSelect.innerHTML = ""

    let user
    users.forEach(userTmp => {
        if (userTmp[0] === userId) {
            user = userTmp
        }
    });

    roles.forEach((role) => {
        if (user) {
            if (user[4] !== role[1]) {
                let newOption = document.createElement("option")
                newOption.setAttribute("value", role[0])
                newOption.textContent = role[1]
                dialogSelect.appendChild(newOption)
            }  
        } else {
            let newOption = document.createElement("option")
            newOption.setAttribute("value", role[0])
            newOption.textContent = role[1]
            dialogSelect.appendChild(newOption)
        }
    })
}

function setTableData(users) {
    const table = document.getElementById("user-table")
    users.forEach((user, index1) => {
        let newRow = document.createElement("tr")
        const userObj = Object.values(user)
        console.log(userObj)
        for (let index2 = 1; index2 < userObj.length + 1; index2++) {
            const value = userObj[index2];
            
            let cell = document.createElement("td");
            if (index2 === 5) {
                cell.classList.add('isActive')
                let cell2
                if (value === true) {
                    cell2 = document.createElement("i")
                    cell2.classList.add("fa-solid")
                    cell2.classList.add("fa-check")
                    cell.appendChild(cell2)
                } else {
                    cell2 = document.createElement("i")
                    cell2.classList.add("fa-solid")
                    cell2.classList.add("fa-xmark")
                    cell.appendChild(cell2)
                }
            } else if (index2 === 6) {
                cell.innerHTML +=
                    '<div class="dropdown">' +
                        '<button onclick="handleDropdown(' + index1 + ')" class="dropbtn">Actions</button>' +
                        '<div id="myDropdown_' + index1 + '" class="dropdown-contentn">' +
                            '<a class="clickable" onclick="modifyUserOpen(\'' + userObj[0] + '\')">Modify User</a>' +
                            '<a class="clickable" onclick="promoteUserOpen(\'' + userObj[0] + '\')">Promote User</a>' +
                            '<a class="clickable" onclick="deleteUser(\'' + userObj[0] + '\')">Delete User</a>' +
                        '</div>' +
                    '</div>'
            } else {
                cell.innerText = value
            }
            newRow.appendChild(cell)
        }
        table.appendChild(newRow)
    });
}

function promoteUserOpen(id) {
    const userId = id
    const promoteDialog = document.getElementById('promote-user');
    const promoteUserBtn = document.getElementById('promote-user-btn');
    const closeBtn = document.getElementById('promote-close-dialog');
    const select = document.getElementById('roles-select')

    setRoleDialog(roles, userId)
    
    closeBtn.addEventListener('click', () => {
        promoteDialog.close();
    });
    
    promoteUserBtn.addEventListener('click', () => {
        console.log(select.value)
        $.ajax({
            url: "/secure_api/promote_user",
            type: 'POST',
            data: {
                "userId": userId,
                "roleId": select.value
            },
            success: function(data) {
                promoteDialog.close();
                location.reload()
            },
            error: function(error) {
                console.error(error)
            },
            beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
        });
    });
    
    promoteDialog.showModal();
}

function modifyUserOpen(id) {
    const userId = id
    const modifyUserDialog = document.getElementById('modify-user');
    const modifyUserBtn = document.getElementById('modify-user-btn');
    const closeBtn = document.getElementById('modify-close-dialog');
    
    closeBtn.addEventListener('click', () => {
        modifyUserDialog.close();
    });
    
    modifyUserBtn.addEventListener('click', () => {
        modifyUserDialog.close();
    });
    
    modifyUserDialog.showModal();
}

function deleteUser(id) {
    const userId = id
    const deleteDialog = document.getElementById('delete-user');
    const deleteUserBtn = document.getElementById('delete-user-btn');
    const closeBtn = document.getElementById('delete-close-dialog');
    
    closeBtn.addEventListener('click', () => {
        deleteDialog.close();
    });
    
    deleteUserBtn.addEventListener('click', () => {
        $.ajax({
            url: "/secure_api/delete_user",
            type: 'POST',
            data: {
                "userId": userId
            },
            success: function(data) {
                deleteDialog.close();
                location.reload()
            },
            error: function(error) {
                console.error(error)
            },
            beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
        });
    });
    
    deleteDialog.showModal();
}

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function handleDropdown(id) {
    document.getElementById("myDropdown_" + id).classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-contentn");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }