using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameControllerScript : MonoBehaviour {

	public Text displayText;
	public InputField InputField;
	public Button PlayAgainButton;

	int numberToGuess;
	int guessCount;
	string guess;
	int guessInt;

	// Use this for initialization
	void Start () {
		PlayAgain ();

	}

	public void GetInput(){
		guess = InputField.text;
		guessCount++;
		CompareGuess ();
		InputField.text = "";
		InputField.ActivateInputField();
	}
		
	public void CompareGuess(){
		guessInt = int.Parse (guess);
		if (guessInt > numberToGuess) {
			displayText.text = "Your guess is higher than my number";
		} else if (guessInt < numberToGuess) {
			displayText.text = "Your guess is lower than my number";
		} else {
			PlayAgainButton.gameObject.SetActive (true);
			displayText.text = "You Won!!! " + "It takes you " + guessCount + " times to guess!";
		}
	}

	public void PlayAgain (){
		numberToGuess = Random.Range (0, 100);
		displayText.text = "Guess a number between 0 - 100";
		PlayAgainButton.gameObject.SetActive (false);
		guessCount = 0;
	}
}
