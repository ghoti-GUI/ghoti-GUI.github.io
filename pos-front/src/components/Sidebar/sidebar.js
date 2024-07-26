import React, { useState } from 'react';
import { FaHome, FaInfoCircle, FaServicestack, FaEnvelope } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import { multiLanguageText } from '../../multiLanguageText/multiLanguageText.js';
import { Language } from '../../userInfo';
import { fetchAllProduct } from '../../service/product';
import { fetchAllCategory } from '../../service/category';
import ExportButton from '../ExportButton/exportButton';
import ChangeExportRuleButton from '../ChangeExportRuleButton/changeExportRuleButton';
import ImportButton from '../ImportButton/importButton';

const Sidebar = () => {
  const Text = {...multiLanguageText}[Language].sidebar;
  const [sidebarChoosed, setSidebarChoosed] = useState('')

  return (
    <div className="h-screen w-64 bg-gray-800 text-white">
      <div className="p-4">
        <h1 className="text-2xl font-bold">{Text.title}</h1>
      </div>
      <nav className="mt-10">
        <Link 
          to="" 
          className={`flex items-center px-4 py-2 hover:bg-gray-700 w-full ${sidebarChoosed==='home'?'bg-gray-600':''}`} 
          onClick={()=>{setSidebarChoosed('home')}}>
          <FaHome className='mr-2'/>
          {Text.home}
        </Link>
        <Link 
          to="addCategory" 
          className={`flex items-center px-4 py-2 hover:bg-gray-700 w-full ${sidebarChoosed==='addCategory'?'bg-gray-600':''}`} 
          onClick={()=>{setSidebarChoosed('addCategory')}}>
          <FaInfoCircle className='mr-2'/>
          {Text.addCategory}
        </Link>
        <Link 
          to="add/Product" 
          className={`flex items-center px-4 py-2 hover:bg-gray-700 w-full ${sidebarChoosed==='addProduct'?'bg-gray-600':''}`} 
          onClick={()=>{setSidebarChoosed('addProduct')}}>
          <FaInfoCircle className='mr-2'/>
          {Text.addProduct}
        </Link>
        <div className='flex flex-col items-center justify-center w-full mt-10'>
          <ImportButton/>
          <ExportButton/>
          <ChangeExportRuleButton/>
        </div>
      </nav>
    </div>
  );
}

export default Sidebar;