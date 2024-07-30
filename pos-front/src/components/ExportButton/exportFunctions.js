import React, { useContext, useEffect, useState } from 'react';
import { fetchAllProduct } from "../../service/product";
import { fetchAllCategory } from "../../service/category";
import { multiLanguageText } from '../../multiLanguageText/multiLanguageText.js';
import { Language, UserContext } from '../../userInfo';
import { useSearchParams } from 'react-router-dom';
// import { handleClickExport } from './export';
import JSZip from 'jszip';
import { saveAs } from 'file-saver';
import { lengthContent, lengthID } from '../../service/valueDefault';
import { fetchAllTVA, fetchTVA } from '../../service/tva.js';


const initAbList = {
    'ab1.txt':'',
    'ab2.txt':'',
    'ab3.txt':'',
    'ab4.txt':'',
    'ab5.txt':'',
    'ab6.txt':'',
    'ab7.txt':'',
    'ab8.txt':'',
    'ab9.txt':'',
    'ab10.txt':'',
    'ab11.txt':'',
    'ab12.txt':'',
    'ab13.txt':'',
    'ab14.txt':'',
    'met.txt':'',
};
const initZwcdValue = ''
const initRiscdValue = ''
const initHooftNameValue = {
    'ab1.txt':'',
    'ab2.txt':'',
    'ab3.txt':'',
    'ab4.txt':'',
    'ab5.txt':'',
    'ab6.txt':'',
    'ab7.txt':'',
    'ab8.txt':'',
    'ab9.txt':'',
    'ab10.txt':'',
    'ab11.txt':'',
    'ab12.txt':'',
    'ab13.txt':'',
    'ab14.txt':'',
};

export const fetchData=async(fetch=true, productsData=null, categoriesData=null)=>{

    const productsRecv = fetch?await fetchAllProduct():productsData;
    const categoriesRecv = fetch?await fetchAllCategory():categoriesData;
    const tvaRecv = await fetchAllTVA();
    console.log('tvaRecv:', tvaRecv)
    let abListCopy = { ...initAbList };
    let zwcdValueCopy = initZwcdValue;
    let zwwmValueCopy = initZwcdValue;
    let riscdValueCopy = initRiscdValue;
    let riswmValueCopy = initRiscdValue;
    

    productsRecv.forEach((product, index) => {
        const Xu_class = product.Xu_class
        if(!Object.keys(abListCopy).includes(Xu_class)){
            abListCopy[Xu_class]='';
        }
        abListCopy[product.Xu_class] += formatProductData(product, tvaRecv)+'\n';

        const dinein_takeaway = product.dinein_takeaway
        if (dinein_takeaway === 1){
            zwcdValueCopy += formatKitchenData(product);
            riscdValueCopy += formatPrintData(product);
        }else if(dinein_takeaway === 2){
            zwwmValueCopy += formatKitchenData(product);
            riswmValueCopy += formatPrintData(product);
        }
    });

    let HooftNameValueCopy = {...initHooftNameValue};
    categoriesRecv.forEach((category, index) => {
        if(category.Xu_class!=='met.txt'){
            const name = category.name||category.ename||category.lname||category.fname||category.zname;
            if(!Object.keys(HooftNameValueCopy).includes(category.Xu_class)){
                HooftNameValueCopy[category.Xu_class] = '';
            }
            HooftNameValueCopy[category.Xu_class] += ' '+name;
        }
    });

    // 给HooftName添加void
    for(let [key, value] of Object.entries(HooftNameValueCopy)){
        if(!value) HooftNameValueCopy[key]+=' void';
    };
    console.log(HooftNameValueCopy)
    return [
        productsRecv, 
        categoriesRecv, 
        abListCopy, 
        zwcdValueCopy, 
        zwwmValueCopy, 
        riscdValueCopy, 
        riswmValueCopy, 
        HooftNameValueCopy
    ]

};

const formatProductData = (product, tva_list) => {
    const id_XuRecv = product.id_Xu.toString();
    const id_Xu = id_XuRecv==='hyphen3'?'---':id_XuRecv.padStart(lengthID, ' ');
    const bill_content = product.bill_content+'.'.padEnd(lengthContent-product.bill_content.length, ' ');
    const price = product.price;
    const tva = tva_list.find(tva => tva.id === product.TVA_id)
    let tva_category = 'A';
    if(tva){
        switch (tva.category){
            case 1:
                tva_category = 'A';
                break;
            case 2:
                tva_category = 'B';
                break;
            case 3:
                tva_category = 'C';
                break;
            case 4:
                tva_category = 'D';
                break;
            default:
                tva_category = 'A';
        }
    }
    return `${id_Xu} ${bill_content} ${price} ${tva_category}`;
};

const formatKitchenData = (product) => {
    const id_Xu = product.id_Xu.toString().padStart(lengthID, ' ');
    const kitchen_content = product.kitchen_content;
    return `${id_Xu} ${kitchen_content}\n`;
};

const formatPrintData = (product) => {
    let printerData = '';
    const printers = product.print_to_where
    for(const printer of printers.toString()){
        const kitchen_content = product.kitchen_content;
        printerData += `${printer} ${kitchen_content}\n`;
    }
    return printerData;
};

export const createFile = async(handle, name, value)=>{
    const newFileHandle = await handle.getFileHandle(name, { create: true });
    const writable = await newFileHandle.createWritable();
    await writable.write(value);
    await writable.close();
}


export const exportFileAfterImport = async(productsData, categoriesData)=>{
    console.log('exporting')
    try{
        const handle = await window.showDirectoryPicker();
        const [productsRecv, categoriesRecv, abListCopy, zwcdValueCopy, HooftNameValueCopy] = await fetchData(false, productsData, categoriesData);
        for (const [key, value] of Object.entries(abListCopy)){
            createFile(handle, `${key}`, value)
        }
        createFile(handle, 'zwcd.txt', zwcdValueCopy)

        let valueHooft = 'Contents\n'
        for (const [key, value] of Object.entries(HooftNameValueCopy)){
            valueHooft+=`${key}${value}\n`;
        }
        createFile(handle, 'HooftName.txt', valueHooft)

        alert('File downloaded successfully!');
    }catch(e){
        console.error('Error downloading file:', e);
    }
}