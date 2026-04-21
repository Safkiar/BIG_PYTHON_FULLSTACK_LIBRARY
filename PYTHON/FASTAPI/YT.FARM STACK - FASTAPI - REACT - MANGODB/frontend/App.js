import { useEffect, useState } from "react";
import axios from "axios"
import "./App.css";
import ListToDoLists from "./ListTodoLists";
import toDoList from "./ToDoList";

function App() {
    const [listSummaries, setListSummaries] = useState(null);
    const [selectionItem, setSelectedItem] = useState(null);

    useEffect(() => {
        reloadData().catch(console.error)
    }, [])

    async function reloadData() {
        const response = await axios.get("/api/lists");
        const data = await response.data; 
        setListSummaries(data);
    }

    function handleNewToDoList(newName){
        const updateDate = async() => {
            const newListData = {
                name: newName,
            };
            await axios.post('/api/lists', newListData);
            reloadData().catch(console.error);
        };
        updateDate();
    }
    function handleSelectList(id) {
        console.log("Selecting item", id);
        setSelectedItem(id)
    }
    function backToList() {
        setSelectedItem(null);
        reloadData().catch(console.error);
    }

    if (selectedItem === null) {
        return (
            <div className="App">
                <ListToDoLists 
                listSummaries={listSummaries}
                handleSelectList={handleSelectList}
                handleNewToDoList={handleNewToDoList}
                handleDeleteToDoList={handleDeleteToDoList}
                />
            </div>
        );
    } else {
        return (
            <div className="App">
                <ToDoList listId={selectedItem} handleBackButton={backToList}/>
            </div>
        )
    }
}

export default App