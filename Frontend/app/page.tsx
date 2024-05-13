'use client'
import { useState } from "react"
import { useForm, SubmitHandler } from "react-hook-form"

type Inputs = {
  question: string
  exampleRequired?: string
}

export default function Home() {

  const [message, setMessage] = useState('');
  const [write, setWrite] = useState('');

  const wrtieHandle = (e: any) => {
    setWrite(e.target.value);
  }
  
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = (data) => {
    console.log('입력된 값 : ' + JSON.stringify(data))
    fetch('http://localhost:8000/api/chat/titanic', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json()) // JSON 형식으로 파싱
      .then((data) => setMessage(data.titanic)) // 파싱된 데이터 콘솔 출력
      .catch((error) => console.log("error:", error));
  }

  console.log(watch("question")) // watch input value by passing the name of it


  return (
    
<div className="w-[3000px] h-[1500px] relative bg-white">
  <div className="w-[700px] h-[700px] left-[700px] top-[400px] absolute bg-white">
    <div className="h-[1000px] left-[24px] top-[-48px] absolute flex-col justify-start items-start gap-[35px] inline-flex">
      <div className="self-stretch h-12" />
      <div className="self-stretch h-40 flex-col justify-start items-start gap-2 flex">
        <div className="px-4 py-3 bg-neutral-200 rounded-tl-3xl rounded-tr-2xl rounded-bl rounded-br-2xl justify-center items-center gap-2 inline-flex">
          <div className="grow shrink basis-0 text-black text-base font-medium font-['Inter'] leading-normal">{write}</div>
        </div>
      </div>
      <div className="self-stretch h-[184px] flex-col justify-start items-end gap-2 flex">
        <div className="px-4 py-3 bg-black rounded-tl-2xl rounded-tr-2xl rounded-bl-2xl rounded-br justify-center items-center gap-2 inline-flex">
          <div className="grow shrink basis-0 text-white text-base font-medium font-['Inter'] leading-normal">{message ? message : ""}</div>
        </div>
        
      </div>
      <div className="self-stretch h-40 flex-col justify-start items-start gap-2 flex">
        <div className="px-4 py-3 bg-neutral-200 rounded-tl-3xl rounded-tr-2xl rounded-bl rounded-br-2xl justify-center items-center gap-2 inline-flex">
          <div className="grow shrink basis-0 text-black text-base font-medium font-['Inter'] leading-normal">넌 최고야</div>
        </div>

      </div>
    </div>
  </div>
  <div className="left-[1203px] top-[19px] absolute justify-start items-start inline-flex">
    <div className="p-1 bg-neutral-100 rounded-lg justify-start items-start flex">
      <div className="w-[65px] px-3 bg-white rounded shadow justify-start items-center gap-2 flex">
        <button className="text-black text-base font-medium font-['Inter'] leading-normal">titanic</button>
      </div>
      <div className="w-[67px] px-3 rounded justify-start items-center gap-2 flex">
        <button className="text-black text-base font-medium font-['Inter'] leading-normal">Tab 2</button>
      </div>
      <div className="w-[67px] px-3 rounded justify-start items-center gap-2 flex">
        <button className="text-black text-base font-medium font-['Inter'] leading-normal">Tab 3</button>
      </div>
    </div>

  </div>
    
  <div className="flex items-center justify-center h-screen">
  <form className="max-w-md mx-auto" onSubmit={handleSubmit(onSubmit)}>   
    <label htmlFor="default-search" className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
    <div className="relative">
        <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <svg className="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
            </svg>
        </div>
        <input  {...register("question", { required: true })} onChange={wrtieHandle} type="search" id="default-search" className="block w-full p-4 ps-10 text-sm 
        text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 
        dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
        placeholder="Search Mockups, Logos..." required />
        <button type="submit" className="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none 
        focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
    </div>
    {errors.question && <span>This field is required</span>}
</form>
</div>

  


  
  <div className="h-[280px] left-[650px] top-[19px] absolute flex-col justify-center items-center gap-6 inline-flex">
    <div className="self-stretch text-center text-black text-[64px] font-bold font-['Inter']">Chat Bot</div>
    <div className="w-32 h-32 relative bg-neutral-100 rounded-full">
      <img className="w-32 h-32 left-0 top-0 absolute" src="https://i.ibb.co/3493r17/cat.jpg" />
    </div>
    <div className="self-stretch text-center text-zinc-500 text-2xl font-normal font-['Inter'] leading-9">Ask anything about ~~</div>
  </div>
</div>


  );
}