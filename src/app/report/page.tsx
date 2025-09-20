"use client";

export default function ReportPage() {
  const downloadReport = async () => {
    const res = await fetch("/api/report");
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "report.pdf";
    a.click();
  };

  return (
    <div className="p-6 flex flex-col items-center">
      <h1 className="text-2xl font-bold">Job-Ready PDF Report</h1>
      <p className="mt-2 text-gray-600">
        Click below to generate a server-side PDF.
      </p>
      <button
        onClick={downloadReport}
        className="bg-blue-600 text-white px-6 py-2 rounded-xl shadow-md mt-6 hover:bg-blue-700"
      >
        Download Report
      </button>
    </div>
  );
}
