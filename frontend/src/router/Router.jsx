import React from 'react'
import { Outlet } from 'react-router-dom'


//dev_5
const MainLayout = () => {
  return (
    <div className='vh-100 d-flex flex-column justify-content-between'>
      {/* dev_3_Fruit */}
      <Outlet />
    </div>
  )
}

export default MainLayout