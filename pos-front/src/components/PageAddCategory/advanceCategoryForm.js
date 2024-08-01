import React, { useEffect, useState, useCallback, useContext } from 'react';
import axios, { all } from 'axios';
import { ToastContainer, toast} from 'react-toastify';
import { getCsrfToken } from '../../service/token';
import { DefaultUrl, CheckIdXuExistenceUrl } from '../../service/valueDefault';
// import { checkIdXuExistence} from '../../service/product';
import { fetchAllCategory } from '../../service/category';
import { fetchPrinter } from '../../service/printer';
import { fetchTVA } from '../../service/tva';
import { multiLanguageText, multiLanguageAllergen } from '../../multiLanguageText/multiLanguageText';
import { normalizeText, sortStringOfNumber, mergeObject, updateCheckboxData, updateObject, truncateString } from '../utils';
import { Country, UserContext } from '../../userInfo';
import { addProductModelAdvance } from '../../models/product';

const AdvanceCategoryForm = () => {
    // const Language = localStorage.getItem('Language') || 'English';
    const { Language } = useContext(UserContext);
    return (
        <div>
            
        </div>
    );
}

export default AdvanceCategoryForm;
