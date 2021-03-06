var name = `NadeKing
OpenAI
`;
var url = `https://www.youtube.com/channel/UC5_YHkJ1i5E7E5J5wuU7oyw
https://www.youtube.com/channel/UCXZCJLdBC09xxGZ6gcdrc6A
`;
var folder = `fun `;
function download() {
    
    var folderName = document.getElementById("folder-name").value;
    var bookmarkUrls = document.getElementById("bookmark-urls").value.split("\n");
    var bookmarkNames = document.getElementById("bookmark-names").value.split("\n");
   
    var output = `<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL><p>`
    
    // Only add Folder to output if folder name specified
    if (folderName != "") {
        output = output.concat( `
        <DT><H3>${folderName}</H3>
        <DL><p>`)
    }
    
    for (var i = 0; i < bookmarkUrls.length; i++) {
        
        // Skip blank lines
        if (bookmarkUrls[i] == "") {
            continue;
        }
        
        // Default bookmark name to url string if name not specified
        if (bookmarkNames[i] == "" || typeof bookmarkNames[i] == 'undefined') {
            bookmarkNames[i] = bookmarkUrls[i];
        }
        
        // Add individual bookmark to output
        var bookmark = `
        <DT><A HREF="${bookmarkUrls[i]}">${bookmarkNames[i]}</A>`
        output = output.concat(bookmark)
    }

    if (folderName != "") {
        output = output.concat( `
        </DL><p>`)
    }

    output = output.concat( `</DL><p>`);

    //.html file
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(output));
    element.setAttribute('download', "subscriptions.html");
  
    element.style.display = 'none';
    document.body.appendChild(element);
  
    element.click();
    document.body.removeChild(element);
}
document.getElementById("bookmark-urls").value = url;
document.getElementById("bookmark-names").value = name;
document.getElementById("folder-name").value = folder;