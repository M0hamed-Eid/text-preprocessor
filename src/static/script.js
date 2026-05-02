async function submitText() {
    const text = document.getElementById("inputText").value;
    const language = document.getElementById("language").value;

    const payload = {
        text: text,
        language: language,
        remove_stopwords: document.getElementById("remove_stopwords").checked,
        stemming: document.getElementById("stemming").checked,
        lemmatization: document.getElementById("lemmatization").checked,
        normalization: document.getElementById("normalization").checked
    };

    const response = await fetch("/preprocess", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (response.ok) {
        document.getElementById("originalText").innerText = data.original_text;
        document.getElementById("processedText").innerText = data.processed_text;
    } else {
        alert(data.detail || "Processing failed.");
    }
}