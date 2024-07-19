import { notesUnderID, TimeSupplyData } from "./otherText"

export const ChineseText={
    'country':{
        'Belgium':'比利时',
        'French':'法国', 
    }, 
    'sidebar':{
        'title':'侧栏',
        'home':'主页',
        'addCategory':'添加产品类别',
        'addProduct':'添加产品',
    },
    'product':{
        'id_Xu':['ID', '输入产品ID', 'ID已存在', notesUnderID.Chinese],
        'online_content':['在线名字', '输入显示在 “在线应用” 中的名字'],
        'notesForPrintContent':['您可以在下面两个输入框中输入<b>最多25个字符（12个中文）</b>'], 
        'bill_content':['账单内容', '输入显示在 “账单” 中的内容'],
        'kitchen_content':['厨房内容', '输入发送给 “厨房” 的内容'],
        'online_des':['在线描述', '输入显示在 “在线应用” 中的描述'], 
        'price':['价格', '输入堂食价格'],
        'price2':['外卖价格', '输入外卖价格'],
        'TVA_country':['国家', '选择您所在的国家'],
        'TVA_category':['TVA（税）'],
        'product_type':['类型',{
            '商品':0,
            '选项':1,
          }],
        'cid':['产品类别', '选择产品类别'],
        'time_supply':['供应时间', TimeSupplyData.Chinese, '请选择至少一个供应时间'],
        'print_to_where':['打印机选择','','请选择至少一个打印机'], 
        'advanceButton':'高级设置', 
        'returnNormalButton':'返回一般设置', 
        'submitButton':'添加', 
        'Xu_class':['ab类别'], 
        'add':{
            'pageName':'新增页面',
            'addSuccess':'产品添加成功', 
            'addFailed':'产品添加失败', 
        },
        'check':{
            'pageName':'查看页面', 
            'editButton':'编辑',
        },
        'edit':{
            'pageName':'编辑页面',
            'editSuccess':'编辑成功',
            'editFailed':'编辑失败',
        }, 
        'delete':{
            'deleteButton':'删除', 
            'cancelButton':'取消', 
            'deleteSuccess':['产品 ', ' 删除成功！'],
            'deleteFailed':['产品 ', ' 删除失败！'],
            'confirmDelete':'您确定要删除这个产品吗?',  
        }
        
    },
    'productAdvance':{
        'id_user':['自定义ID', '没有任何限制的自定义ID'],
        'online_content':['在线内容', '请输入在线应用中显示的产品内容'],
        'online_des':['在线描述', '请输入在线应用中显示的产品描述'], 
        'product_type':['产品类型',{
            '产品':0,
            '选项':1,
        }],
        'min_nbr':['最少购买数量','当用户选择购买产品时，用户购买产品的最少数量'],
        'discount':['折扣', ['无', '买一送一','固定降价', '百分比降价']], 
        'allergen':['过敏原'], 
        'ename':['英文名字', '输入英文名字'],
        'lname':['荷兰语名字', '输入荷兰语名字'], 
        'fname':['法语名字', '输入法语名字'], 
        'zname':['中文名字', '输入中文名字'], 
        'edes':['英文描述', '输入英文描述'],
        'ldes':['荷兰语描述', '输入荷兰语描述'],
        'fdes':['法语描述', '输入法语描述'],
        'stb':['Sushi to bar'],
        'favourite':['Favourite'],
        'submitButton':'添加', 
    },
    'category':{
        'id':['ID', '输入类别ID', 'ID已存在', notesUnderID.Chinese],
        'name':['类别名字', '输入新的类别名字'],
        'des':['类别描述', '输入对新的类别的描述'],
        'time_supply':['供应时间', TimeSupplyData.Chinese, '请选择至少一个供应时间'], 
        'addSuccess':'类别添加成功', 
        'addFailed':'类别添加失败', 
        'Xu_class':['ab类别'],
        'nameExisted':'类别名字已存在！', 
    }, 
    'img':{
        'check':'您已选择的图片：',
        'chooseImg':'选择产品的图片', 
        'changeImg':'更改图片', 
    }, 
    'color':{
        'bgcolor':'选择背景颜色: ',
        'text_color':['自动设置字体颜色', ['黑色', '白色']], 
        'textDefault':'文本', 
    }, 
    'home':{
        'id':['ID'],
        'online_content':['在线内容'],
        'bill_content':['账单内容'],
        'kitchen_content':['厨房内容'],
        'online_des':['账单描述'], 
        'price':['价格'],
        'price2':['外卖价格'],
        'TVA':['TVA'],
        'product_type':['类型'],
        'cid':['产品种类'],
        'time_supply':['供应时间',['午餐', '晚餐', '全天']],
        'print_to_where':['打印机选择'], 
        'title':'主页',
        'productList':'产品列表', 
        'modifyOrder':'修改产品顺序',
        'changeFavouriteFailed':'修改收藏失败'
    },
    'dialogChangeOrder':{
        'title':'修改产品顺序',
        'submitButton':'保存',
        'cancelButton':'取消', 
    }, 
    'export':'导出', 
    'returnButton':'返回', 
}


export const ChineseAllergen = [
    '含有麸质的谷物', 
    '甲壳动物产品', 
    '蛋类产品', 
    '花生类产品', 
    '鱼类产品', 
    '大豆制品', 
    '奶制品（包括乳糖）', 
    '坚果及其制品', 
    '芹菜制品', 
    '芥末产品', 
    '芝麻制品', 
    '二氧化硫和亚硫酸盐浓度超过 10 毫克/千克或 10 毫克/升', 
    '羽扇豆产品',
    '软体动物产品', 
]