import React from 'react';
import {Button, TextField} from "@mui/material";

import logo from "./logo.png"
import cl from "./AuthorizationForm.module.css"

const AuthorizationForm = () => {
    return (

        <div className={cl.auth_form}>
            <div className={cl.invitation}>
                <div className={cl.img_block}>
                    <img src={logo} alt="MakMath logo"/>
                </div>


            </div>
            <div className={cl.form_area}>

                <div>
                    <p>Добро пожаловать на MakMath!</p>
                    <p>Войдите, чтобы продолжить.</p>
                </div>
                <TextField label="Введите логин" variant="standard"/>
                <TextField label="Введите пароль" variant="standard"/>
                <Button variant="contained">Войти</Button>
            </div>

        </div>
    );
};

export default AuthorizationForm;