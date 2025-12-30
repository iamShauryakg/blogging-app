import { Routes, Route } from 'react-router-dom'
import './App.css'

import Home from './pages/Home'
import Layout from './Components/Layout'


function App() {

  return (
    <>

    <Routes>
      <Route path="/" element={<Layout />} >
        <Route index element={<Home />} />
        <Route path="/about" element={<div>About Page</div>} />
      </Route>
    </Routes>
    
    </>
  )
}

export default App
