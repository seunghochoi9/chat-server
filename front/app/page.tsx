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
    fetch('http://localhost:8000/titanic', {
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
        <div className="text-black text-base font-medium font-['Inter'] leading-normal">타이타닉</div>
      </div>
      <div className="w-[67px] px-3 rounded justify-start items-center gap-2 flex">
        <div className="text-black text-base font-medium font-['Inter'] leading-normal">Tab 2</div>
      </div>
      <div className="w-[67px] px-3 rounded justify-start items-center gap-2 flex">
        <div className="text-black text-base font-medium font-['Inter'] leading-normal">Tab 3</div>
      </div>
    </div>
  </div>
  
  <div className="w-[827px] h-[101px] px-4 py-2 left-[326px] top-[944px] absolute bg-white rounded-lg border border-neutral-200 justify-start items-center gap-4 inline-flex">
  <form onSubmit={handleSubmit(onSubmit)}>
          <input type="text" {...register("question", { required: true })} className="w-full mb-4 p-3 border border-gray-300 rounded" onChange={wrtieHandle} />
          <button type="submit" className="w-full py-3 bg-blue-500 text-white font-bold rounded">전송</button>
        </form>
        {errors.question && <span>This field is required</span>}
    <div className="grow shrink basis-0 text-zinc-500 text-base font-normal font-['Inter'] leading-normal">Enter your message</div>

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