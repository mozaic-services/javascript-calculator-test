pipeline {
	agent any

	stages {
		stage('Test') {
			steps {
				sh 'calculator-test.sh $ENVIRONMENT'
			}
		}
	}
}

