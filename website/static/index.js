function deletePatient(patientID){
    fetch("/delete-patient", {
        method: 'POST',
        body: JSON.stringify({ patientID: patientID}),
    }).then((_res) => {
        window.location.href="/viewPast";
    });
}