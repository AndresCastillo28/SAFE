import policia from './img/policia.jpg'
import bomberos from './img/bomberos.jpg'
import ambulancia from './img/ambulancia.jpg'
import ejercito from './img/ejercito.jpg'
import './css/styles.css'



export const SafePage = () => {

  const onClick = ( event ) => {
    console.log({ click: event });
  }
  

  return (

    <>
      <nav id="nav" className="navbar bg-light container">
        <div className="container-fluid">
            <span id="logo" className="navbar-brand mb-0 h1 fs-1" style={{color: "#10486e"}}>SAFE</span>
        </div>
        <div className="container-fluid">
            <p className="fs-4" style={{color: "#0b0e10"}}>Seguridad integral y ágil fuente de respuesta ante emergencia
            </p>
        </div>
      </nav>
      <section id="galeria" className="container">
        <div className="row">
            <div className="col-lg-3">
                <img name='policia' src={policia} alt="" onClick={ onClick }/>
            </div>
            <div className="col-lg-3">
                <img src={bomberos} alt="" />
            </div>
            <div className="col-lg-3">
                <img src={ambulancia} alt="" />
            </div>
            <div className="col-lg-3">
                <img src={ejercito} alt="" />
            </div>
        </div>
      </section>
    </>
  )
}
