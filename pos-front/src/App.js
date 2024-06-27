// import logo from './logo.svg';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import './App.css';
import Home from './components/Home/home';
import Sidebar from './components/Sidebar/sidebar';
import AddProduct from './components/PageAddProduct/addProduct';
import AddCategory from './components/PageAddCategory/addCategory';

function App() {
  return (
    <Router>
      <div className='flex bg-slate-200 w-full'>
        <Sidebar className=' w-1/12'/>
        <div className='w-11/12 h-screen overflow-y-hidden'>
          <Routes className='w-full'>
            <Route path='/' element={<Home/>}/>
            <Route path='/addProduct' element={<AddProduct/>}/>
            <Route path='/addCategory' element={<AddCategory/>}/>
          </Routes>
        </div>
      </div>
      <ToastContainer
        position="bottom-center"
        autoClose={3000}
        closeOnClick
        pauseOnFocusLoss={false}/>
    </Router>
    
  );
}

export default App;
