window.onload = function(){
	let num = 0
	let sigButton = document.querySelector('.btnG')
	
	sigButton.addEventListener('click',showVistaTalla)

	function showVistaTalla () {
		let right = document.querySelector('.Wright')
		let left = document.querySelector('.Wleft')
		let registroButton = document.querySelector('.SigButton')
		if (num == 0){
			left.classList.add('hidden')
			right.classList.remove('hidden')
			registroButton.classList.remove('hidden')
			sigButton.textContent = 'Anterior'
			num = 1
		}else{
			left.classList.remove('hidden')
			right.classList.add('hidden')
			registroButton.classList.add('hidden')
			sigButton.textContent = 'Siguiente'
			num = 0
		}
	}
}

