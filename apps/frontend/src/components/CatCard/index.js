import React from "react";
import {Link} from "react-router-dom";

function CatCard(props) {
    return (
        <div className="col-4 col-12-medium">
            <section className="box feature" data-id={props.id}>
                <Link to={`/adopt/${props.id}`} className="image featured"><img src={`${process.env.REACT_APP_API_ROOT}${props.image}`} alt=""  className="img-index"/></Link>
                <div className="inner">
                    <header>
                        <h2>{props.breed}</h2>
                        <p>{props.age}</p>
                    </header>
                <p>{props.color}</p>
                </div>
            </section>
        </div>
    );
}
export default CatCard;