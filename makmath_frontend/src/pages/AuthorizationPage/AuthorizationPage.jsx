import React, {useState} from 'react';
import {Button, IconButton, InputAdornment, TextField} from "@mui/material";

import logo from "./logo.png"
import cl from "./AuthorizationPage.module.css"
import axios from "axios";
import {Visibility, VisibilityOff} from "@mui/icons-material";

const AuthorizationPage = () => {

    const [userData, setUserdata] = useState({login: "", password: ""})
    // Add these variables to your component to track the state
    const [showPassword, setShowPassword] = useState(false);
    const handleClickShowPassword = () => setShowPassword(!showPassword);
    const handleMouseDownPassword = () => setShowPassword(!showPassword);

    return (
        <div className={cl.auth_body}>

            <div className={cl.area}>
                <div className={cl.img_block}>
                    <img src={logo} alt="MakMath logo"/>
                </div>
                <div className={cl.invitation}>
                    <p>Добро пожаловать на MakMath!</p>
                    <p>Войдите, чтобы продолжить.</p>
                </div>
                <div className={cl.auth_form}>
                    <TextField label="Введите логин"
                               onChange={(e) => setUserdata({login: e.target.value, password: userData.password})}
                               variant="standard"/><br/>
                    <TextField label="Введите пароль"
                               type={showPassword ? "text" : "password"}
                               InputProps={{ // <-- This is where the toggle button is added.
                                   endAdornment: (
                                       <InputAdornment position="end">
                                           <IconButton
                                               aria-label="toggle password visibility"
                                               onClick={handleClickShowPassword}
                                               onMouseDown={handleMouseDownPassword}
                                           >
                                               {showPassword ? <Visibility/> : <VisibilityOff/>}
                                           </IconButton>
                                       </InputAdornment>
                                   )
                               }}
                               onChange={(e) => setUserdata({login: userData.login, password: e.target.value})}
                               variant="standard"/><br/>
                    <Button style={{
                        borderRadius: 15,
                        backgroundColor: "#1e7e98",
                        padding: "18px 36px",
                        fontSize: "18px"
                    }} variant="contained" onClick={() => {
                        axios
                            .post("http://localhost:8000/users/login",
                                {username: userData.login, password: userData.password})
                            .then((res) => {
                                if (res.status === 202){
                                    alert("Вы вошли успешно!")
                                    window.location.href = "/home"
                                }
                            })
                            .catch((ex) => {
                                alert("Ошибка доступа!" + ex.toString())
                            });


                    }}>Войти</Button>

                </div>

            </div>

        </div>
    );
};

export default AuthorizationPage;