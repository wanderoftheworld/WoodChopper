import React, { useState } from 'react';

const CustomDrawer = ({ children }) => {
  const classes = useStyles();
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => {
    setIsOpen(false);
  };

  return (
    <div className={isOpen ? classes.drawerOpen : classes.drawerClose}>
      <div className={classes.drawerContent}>
        {children}
        <button className={classes.closeButton} onClick={handleClose}>
          Close
        </button>
      </div>
    </div>
  );
};

function App() {
  return (
    <CustomDrawer />
  );
}
export default App;
