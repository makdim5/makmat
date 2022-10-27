import React from 'react';
import cl from "./FeatureScene.module.css"
import pict from './pict.png'

const FeatureScene = () => {



        return (
            <div className={cl.feature}>

                <div className={cl.img_block}>
                    {/* eslint-disable-next-line jsx-a11y/img-redundant-alt */}
                    <img src={pict} alt="Feature picture"/>
                </div>
                <div className={cl.text_block}>
                    <div className={cl.feature_name}>Интерактивные средства обучения!</div>
                    <div className={cl.description}>Многие математические модели реализованы в виде интерактивных приложений,
                        которые легко можно опробовать на сайте!
                    </div>
                </div>

            </div>
        );
    }
;

export default FeatureScene;