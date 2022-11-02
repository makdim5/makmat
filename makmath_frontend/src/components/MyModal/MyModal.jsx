import React, {useState} from 'react';
import classes from "./MyModal.module.css"

const MyModal = ({children, visible, setVisible}) => {

    const rootClasses = [classes.myModel]
    if(visible){
        rootClasses.push(classes.active)
    }

    return (
        <div className={rootClasses.join(' ')} onClick={() => setVisible(false)}>
            <div className={classes.myModelContent} onClick={e => e.stopPropagation()}>
                {children}
            </div>

        </div>
    );
};

export default MyModal;