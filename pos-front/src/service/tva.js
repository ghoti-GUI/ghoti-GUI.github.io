import axios from 'axios';
import { DefaultUrl, GetTVACountryUrl } from './valueDefault';


// fetch tva data dor add product form
export const fetchTVA = async () =>{
    try {
        const response = await axios.get(DefaultUrl+GetTVACountryUrl);
        const TVAData = response.data; //Dutch: {21.00%: 1, 9.00%: 2, 0.00%: 3}
        // console.log(TVAData)
        return TVAData
    } catch (error){
        console.error('Error fetching TVA data:', error)
    }
}

export const fetchAllTVA = async () =>{
    try {
        const response = await axios.get(DefaultUrl+'get/tva/all/');
        const TVAData = response.data; //Dutch: {21.00%: 1, 9.00%: 2, 0.00%: 3}
        // console.log(TVAData)
        return TVAData
    } catch (error){
        console.error('Error fetching TVA data:', error)
    }
}

export const fetchTVAById = async (TVA_id) =>{
    try{
        const response = await axios.get(DefaultUrl+'get/tva/by_id/', {
            params:{
                'TVA_id':TVA_id, 
            }
        })
        const TVAData = response.data
        return TVAData
    }catch (error){
        console.error('Error fetching TVA data by id:', error)
    }
}

export const fetchTVAIdByCountryCategory = async (tva_country, tva_category) =>{
    try{
        const response = await axios.get(DefaultUrl+'get/tva_id/by_country_category/', {
            params:{
                'tva_country':tva_country, 
                'tva_category':tva_category, 
            }
        })
        const TVAData = response.data
        return TVAData
    }catch (error){
        console.error('Error fetching TVA data by id:', error)
    }
}
