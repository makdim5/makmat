import React, {useEffect, useState} from 'react';
import {Button, IconButton, InputAdornment, TextField} from "@mui/material";
import logo from "./logo.png"
import cl from "./AuthorizationPage.module.css"
import {Visibility, VisibilityOff} from "@mui/icons-material";


const AuthorizationPage = () => {

    const [access, setAccess] = useState(localStorage.getItem('accessToken'))
    const [refresh, setRefresh] = useState(localStorage.getItem('refreshToken'))
    const [refreshRequired, setRefreshRequired] = useState(false)
    const [loading, setLoading] = useState()
    const [formUsername, setFormUsername] = useState()
    const [formPassword, setFormPassword] = useState()
    const [error, setError] = useState()

    // Add these variables to your component to track the state
    const [showPassword, setShowPassword] = useState(false);
    const handleClickShowPassword = () => setShowPassword(!showPassword);
    const handleMouseDownPassword = () => setShowPassword(!showPassword);

    const MY_URI = "http://localhost:8000/users/current"

    useEffect(() => {
        if (access) {
            fetch(
                MY_URI,
                {
                    headers: {
                        'Content-Type': 'application/json;charset=utf-8',
                        'Authorization': `Bearer ${access}`,
                    },
                }
            ).then(response => {
                if (response.ok) {
                    return response.json()
                } else {
                    if (response.status === 401) {
                        throw Error('refresh')
                    }
                    throw Error(`Something went wrong: code ${response.status}`)
                }

            }).then(({data}) => {
                console.log(data)

                alert(`${data.username}, вы вошли успешно!`)
                // window.location.href = "/"
            }).catch(error => {
                if (error.message === 'refresh') {
                    setRefreshRequired(true)
                } else {
                    console.log(error)
                    setError('Ошибка, подробности в консоли')
                }
            })
        }
    }, [access])

    useEffect(() => {
        if (refreshRequired) {
            fetch(
                'http://localhost:8000/api/token/refresh',
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json;charset=utf-8',
                    },
                    body: JSON.stringify({refresh})
                }
            )
                .then(response => {
                    if (response.ok) {
                        return response.json()
                    } else {
                        throw Error(`Something went wrong: code ${response.status}`)
                    }
                })
                .then(({access, refresh}) => {
                    localStorage.setItem('accessToken', access)
                    setAccess(access)
                    localStorage.setItem('refreshToken', refresh)
                    setRefresh(refresh)
                    setError(null)
                })
                .catch(error => {
                    console.log(error)
                    setError('Ошибка, подробности в консоли')
                })
        }
    }, [refresh, refreshRequired])

    const submitHandler = e => {
        e.preventDefault();
        setLoading(true);
        fetch(
            'http://localhost:8000/api/token/obtain',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                },
                body: JSON.stringify({
                    username: formUsername,
                    password: formPassword,
                })
            }
        ).then(response => {
            if (response.ok) {
                return response.json()
            } else {
                throw Error(`Something went wrong: code ${response.status}`)
            }
        }).then(({access, refresh}) => {
            localStorage.setItem('accessToken', access)
            setAccess(access)
            localStorage.setItem('refreshToken', refresh)
            setRefresh(refresh)
            setError(null)

        }).catch(error => {
            console.log(error)
            setError('Ошибка, подробности в консоли')
        }).finally(setLoading(false))
    }

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
                               name="username" value={formUsername}
                               onChange={e => setFormUsername(e.target.value)}
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
                               name="password" value={formPassword}
                               onChange={e => setFormPassword(e.target.value)}
                               variant="standard"/><br/>
                    <Button style={{
                        borderRadius: 15,
                        backgroundColor: "#1e7e98",
                        padding: "18px 36px",
                        fontSize: "18px"
                    }} variant="contained" onClick={submitHandler}>Войти</Button>
                </div>
            </div>
        </div>
    );
};

export default AuthorizationPage;