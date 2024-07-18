import { notesUnderID, TimeSupplyData } from "./otherText"


export const EnglishText = {
    'country':{
        'Belgium':'Belgium',
        'French':'French', 
    }, 
    'sidebar':{
        'title':'Sidebar',
        'home':'Home',
        'addCategory':'AddCategory',
        'addProduct':'AddProduct',
    },
    'product':{
        // 'id_Xu':['ID', 'Enter your product\'s ID', 'ID can be entered up to <b>&nbsp three digits &nbsp</b> in <b>&nbsp letters &nbsp</b> and <b>&nbsp numbers &nbsp</b>'],
        'id_Xu':['ID', 'Enter your product\'s ID', 'ID already existed', notesUnderID.English],
        'notesForPrintContent':['You can enter up to <b>25 characters</b> for the two contents below'], 
        'bill_content':['Bill content', 'Enter the content shown on the bill'],
        'kitchen_content':['Kitchen content', 'Enter the content to send to the kitchen'],
        'price':['Price', 'Enter the price for eat in'],
        'price2':['Price for takeaway', 'Enter the price for takeaway'],
        'TVA_country':['Country', 'Select your country here'],
        'TVA_category':['TVA'],
        'cid':['Category', 'Select the category of this product'],
        'time_supply':['Supply time', {
            'lunch': true,
            'dinner': true,
        }, 'Please choose at least one supply time'],
        'print_to_where':['Printers selected','','Please select at least one printer'], 
        'advanceButton':'Advance settings', 
        'returnNormalButton':'Return to normal settings', 
        'submitButton':'Submit', 
        'Xu_class':['Category-ab'], 
        'add':{
            'pageName':'Add Product',
            'addSuccess':'Product added successfully', 
            'addFailed':'Product added failed', 
        }, 
        'check':{
            'pageName':'Check Product', 
            'editButton':'Edit',
        },
        'edit':{
            'pageName':'Edit Product',
            'editSuccess':'Edit succeed!',
            'editFailed':'Edit failed!',
        }, 
        'delete':{
            'deleteButton':'Delete', 
            'cancelButton':'Cancel', 
            'deleteSuccess':['product ', ' deleted successfully.'],
            'deleteFailed':['product ', ' deleted failed.'],
            'confirmDelete':'Are you sure to delete this product?',        
        }
    },
    'productAdvance':{
        'id_user':['ID without restrictions', 'ID without any restrictions'],
        'online_content':['Online content', 'Enter the content shown in the online application'],
        'online_des':['Online description', 'Enter the description shown online'], 
        'product_type':['Type',{
            'Product':0,
            'Option':1,
        }],
        'min_nbr':['Minimum number of purchase','The minimum number of products purchased by the user when the user selects a product to purchase'],
        'discount':['Discount', ['None', 'Buy 1 Get 1 Free','Fixed reduction', 'Percentage reduction']], 
        'allergen':['Allergen'], 
        'ename':['English name', 'Enter the name in English'],
        'lname':['Dutch name', 'Enter the name in Dutch'], 
        'fname':['French name', 'Enter the name in French'], 
        'zname':['Chinese name', 'Enter the name in Chinese'], 
        'edes':['English description', 'Enter the description in English'],
        'ldes':['Dutch description', 'Enter the description in Dutch'],
        'fdes':['French description', 'Enter the description in French'],
        'stb':['Sushi to bar'],
        'favourite':['Favourite'],
        'submitButton':'Submit', 
    },
    'category':{
        'id':['ID', 'Enter the ID of your new category', 'ID already existed', notesUnderID.English],
        'name':['Name', 'Enter the name of your new category'],
        'des':['Description', 'Enter the description of your new category'],
        'time_supply':['Supply time', TimeSupplyData.English, 'Please choose at least one supply time'], 
        'addSuccess':'Category added successfully', 
        'addFailed':'Category added failed', 
        'Xu_class':['Category-ab', 'Choose the category ab1 - ab14'],
        'nameExisted':'The category name already existed ! ', 
    }, 
    'img':{
        'check':'Your choosed image: ',
        'chooseImg':'Choose image for your product', 
        'changeImg':'Change image', 
    }, 
    'color':{
        'bgcolor':'Choose background color: ', 
        'text_color':['Automatic setting for text colours', ['Black', 'white']],
        'textDefault':'Text',
    }, 
    
    'home':{
        'id':['ID'],
        'online_content':['Online content'],
        'bill_content':['Bill content'],
        'kitchen_content':['Kitchen content'],
        'online_des':['Bill description'], 
        'price':['Price'],
        'price2':['Price for takeaway'],
        'TVA':['TVA'],
        'product_type':['Type'],
        'cid':['Category'],
        'time_supply':['Supply time', ['Lunch', 'Dinner', 'Whole day']],
        'print_to_where':['Printers selected'], 
        'title':'Home',
        'productList':'Product List', 
        'modifyOrder':'Modify product order',
        'changeFavouriteFailed':'Failed to modify favourite'
    },
    'dialogChangeOrder':{
        'title':'Change product order',
        'submitButton':'Submit',
        'cancelButton':'Cancel', 
    }, 
    'export':'Export', 
}


export const EnglishAllergen = [
    'Cereals container of gluten', 
    'Crustaceans products', 
    'Eggs products', 
    'Peanuts products', 
    'Fish products', 
    'Soybean and soya products', 
    'Milk products (including lactose)', 
    'Nuts and products thereof', 
    'Celery products', 
    'Mustard products', 
    'Sesame and sesame products', 
    'Sulfur dioxide and sulphites in concentrations of more than 10 mg/kg or 10 mg/L',
    'Lupin products', 
    'Molluscs products', 
]