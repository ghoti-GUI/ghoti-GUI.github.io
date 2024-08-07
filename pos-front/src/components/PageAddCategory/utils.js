import axios from "axios"
import { useState } from "react"
import { fetchAllCategory } from "../../service/category"


export const fetchAllCategoryForProductForm = async () => {
    try{
        const categoriesData = await fetchAllCategory()
        let categiriesDataForProductForm = {}
        categoriesData.forEach((category)=>{
            const name = category.ename || category.lname || category.fname || category.zname
            categiriesDataForProductForm[name] = category.id
        })
        return categiriesDataForProductForm
    }catch (error){
        console.error('Error fetching category data in addCategory.utils:', error)
    }
    
}