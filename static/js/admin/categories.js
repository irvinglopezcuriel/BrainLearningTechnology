window.onload = getData()

var categories
var subCategories

function getData() {
    getCategories()
    getSubCategories()
}

function getCategories() {
    $.ajax({
        url: "/secure_api/get_categories",
        type: 'GET',
        success: function(data) {
            categories = data
        },
        error: function(error) {
            console.error(error)
        },
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
    });
}

function getSubCategories() {
    $.ajax({
        url: "/secure_api/get_subcategories",
        type: 'GET',
        success: function(data) {
            subCategories = data
        },
        error: function(error) {
            console.error(error)
        },
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
    });
}

function setCategories(categories) {
    const table = document.getElementById("")
    categories.forEach((category, index1) => {
        let newRow = document.createElement("tr")
        const categoryObj = Object.values(category)
        for (let index2 = 1; index2 < categoryObj.length + 1; index2++) {
            const value = categoryObj[index2];
            
            let cell = document.createElement("td");
            if (index2 === 2) {
                cell.innerHTML +=
                    '<div class="dropdown">' +
                        '<button onclick="handleDropdown(' + index1 + ')" class="dropbtn">Actions</button>' +
                        '<div id="myDropdown_' + index1 + '" class="dropdown-contentn">' +
                            '<a class="clickable" onclick="deleteCategory(\'' + categoryObj[0] + '\')">Delete Category</a>' +
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

function setSubCategories(subcategories) {
    const table = document.getElementById("")
    subcategories.forEach((subcategory, index1) => {
        let newRow = document.createElement("tr")
        const subcategoryObj = Object.values(subcategory)
        for (let index2 = 1; index2 < subcategoryObj.length + 1; index2++) {
            const value = subcategoryObj[index2];
            
            let cell = document.createElement("td");
            if (index2 === 2) {
                cell.innerHTML +=
                    '<div class="dropdown">' +
                        '<button onclick="handleDropdown(' + index1 + ')" class="dropbtn">Actions</button>' +
                        '<div id="myDropdown_' + index1 + '" class="dropdown-contentn">' +
                            '<a class="clickable" onclick="deleteSubCategory(\'' + subcategoryObj[0] + '\')">Delete SubCategory</a>' +
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

function deleteCategory(id) {
    const categoryId = id
    const deleteDialog = document.getElementById('delete-item');
    const deleteItemBtn = document.getElementById('delete-item-btn');
    const closeBtn = document.getElementById('delete-close-dialog');
    
    closeBtn.addEventListener('click', () => {
        deleteDialog.close();
    });
    
    deleteItemBtn.addEventListener('click', () => {
        $.ajax({
            url: "/secure_api/delete_category",
            type: 'POST',
            data: {
                "categoryId": categoryId
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

function deleteSubCategory(id) {
    const subcategoryId = id
    const deleteDialog = document.getElementById('delete-item');
    const deleteItemBtn = document.getElementById('delete-item-btn');
    const closeBtn = document.getElementById('delete-close-dialog');
    
    closeBtn.addEventListener('click', () => {
        deleteDialog.close();
    });
    
    deleteItemBtn.addEventListener('click', () => {
        $.ajax({
            url: "/secure_api/delete_subcategory",
            type: 'POST',
            data: {
                "subcategoryId": subcategoryId
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

function addCategory() {
    const addDialog = document.getElementById('add-category');
    const addCategoryBtn = document.getElementById('add-category-btn');
    const closeBtn = document.getElementById('add-category-close-dialog');
    const input = document.getElementById('name-category')

    closeBtn.addEventListener('click', () => {
        addDialog.close();
    });
    
    addCategoryBtn.addEventListener('click', () => {
        $.ajax({
            url: "/secure_api/add_subcategory",
            type: 'POST',
            data: {
                "name": input.value
            },
            success: function(data) {
                addDialog.close();
                location.reload()
            },
            error: function(error) {
                console.error(error)
            },
            beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
        });
    });
    
    addDialog.showModal();
}

function addSubCategory() {
    const addSubDialog = document.getElementById('add-subcategory');
    const addSubCategoryBtn = document.getElementById('add-subcategory-btn');
    const closeBtn = document.getElementById('add-subcategory-close-dialog');
    const input = document.getElementById('name-subcategory')

    closeBtn.addEventListener('click', () => {
        addSubDialog.close();
    });
    
    addSubCategoryBtn.addEventListener('click', () => {
        $.ajax({
            url: "/secure_api/add_subcategory",
            type: 'POST',
            data: {
                "name": input.value
            },
            success: function(data) {
                addSubDialog.close();
                location.reload()
            },
            error: function(error) {
                console.error(error)
            },
            beforeSend: function(xhr){xhr.setRequestHeader('Authorization', localStorage.getItem("token"));},
        });
    });
    
    addSubDialog.showModal();
}
