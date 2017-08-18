using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameControlnew : MonoBehaviour {

	public Text displayText;
	public Button Lower;
	public Button Higher;
	public Button Yup;
	public Text end;
	public Button PlayAgainButton;
	public Text checktext;

	int min = 0;
	int max = 1000;
	int guessnum;

//	public void getinput(){
//		maxInput = InputField.text;
//		_max = int.Parse (max);
//	}

	public void _Lower(){
		max = guessnum - 1;
		play ();
	}

	public void _Higher(){
		min = guessnum + 1;
		play ();
	}

	public void _Yup(){
		displayText.gameObject.SetActive (false);
		Lower.gameObject.SetActive (false);
		Higher.gameObject.SetActive (false);
		Yup.gameObject.SetActive (false);
		end.gameObject.SetActive (true);
		end.text = "Haha, It's too EASY for me!";
		PlayAgainButton.gameObject.SetActive (true);
	}

	public void playAgain(){
		min = 0;
		max = 1000 ;
		play ();
	}

	public void play(){
		displayText.gameObject.SetActive (true);
		PlayAgainButton.gameObject.SetActive (false);
		end.gameObject.SetActive (false);
		Lower.gameObject.SetActive (true);
		Higher.gameObject.SetActive (true);
		Yup.gameObject.SetActive (true);
		checktext.gameObject.SetActive (false);

		if (min > max) {
			checktext.text = "Your number unavailable!!!";
			checktext.gameObject.SetActive (true);
			displayText.gameObject.SetActive (false);
			end.gameObject.SetActive (false);
			Lower.gameObject.SetActive (false);
			Higher.gameObject.SetActive (false);
			Yup.gameObject.SetActive (false);
			PlayAgainButton.gameObject.SetActive (true);
		}

		guessnum = Random.Range (min,max);
		displayText.text = "Pick a number between 0 and 1000 but don't tell me you Puny Human. Is your number " + guessnum;
	}

	public GameControlnew ();

	// Use this for initialization
	void Start () {
		play ();
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
