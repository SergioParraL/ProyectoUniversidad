// window.onload = function(){
// 	let bu
// }



/*<section class="button_form wrapper ">
	<div id="butSig" class="btnG button_1">Siguiente</div>
	<button class='SigButton hidden' type="submit" value="Registrar">Registrar</button>
</section>*/


function buttonRegEst() {
	let registro = document.querySelector('.SigButton')
	let buttonSig = document.querySelector('#butSig')
	let hiddenClas = registro.classList.contains('hidden')
	let left = document.querySelector('.Wleft')
	let right = document.querySelector('.Wright')
	if (hiddenClas == true) {
		registro.classList.remove('hidden')
		right.classList.remove('hidden')
		left.classList.add('hidden')
		buttonSig.textContent = 'Anterior'
	}else {
		right.classList.add('hidden')
		left.classList.remove('hidden')
		registro.classList.add('hidden')
		buttonSig.textContent = 'Siguiente'
	}
}

function buttonVerEstuRepr(){
	let left = document.querySelector('.Wleft')
	let right = document.querySelector('.Wright')
	let button = document.querySelector('#Ant_Sig')

	if (right.classList.contains('hidden')) {
		left.classList.add('hidden')	
		right.classList.remove('hidden')
		Ant_Sig.textContent = 'Ver: Estudiante'	
	}else {
		left.classList.remove('hidden')	
		right.classList.add('hidden')
		Ant_Sig.textContent = 'Ver: Representante'	
		
	}

}





// let num = 0
	// let sigButton = document.querySelector('.btnG')
	// sigButton.addEventListener('click',TabChange)
	// function TabChange(){
	// 	console.log(num)
	// 	let tab01 = document.querySelector('.Wright')
	// 	let tab02 = document.querySelector('.Wleft')
	// 	let registroButton = document.querySelector('.SigButton')
	// 	if (num == 0){
	// 		tab01.classList.remove('hidden')
	// 		tab02.classList.add('hidden')
	// 		sigButton.textContent = 'Ver: Estudiante'
	// 		if (window.location.href == 'http://127.0.0.1:8000/Registro/Registro_Es/') {
	// 			registroButton.classList.remove('hidden')
	// 			sigButton.textContent = 'Anterior'
	// 		}
	// 		num = 1
	// 	}else{
	// 		tab02.classList.remove('hidden')
	// 		tab01.classList.add('hidden')
	// 		sigButton.textContent = 'Ver: Representante'
	// 		if (window.location.href == 'http://127.0.0.1:8000/Registro/Registro_Es/') {
	// 			registroButton.classList.add('hidden')
	// 			sigButton.textContent = 'Siguiente'
	// 		}
	// 		num = 0
	// 	}
	// }

